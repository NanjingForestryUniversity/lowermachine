import socket
from threading import Thread, Event
from typing import Optional
from time import sleep, time
from queue import Queue
import re


class Server(object):
    def __init__(self):
        self._s = None
        self._listen_th, self._receive_th = None, None
        self.ip, self.port = None, None
        self.client_ip, self.client_port, self.client_s = None, None, None
        self._last_heartbeat = None
        self._closing_callback = None
        self._closing_signal = None
        self._connected_callback = None
        self._connected_signal = None
        self._disconnected_callback = None
        self._disconnected_signal = None
        self._send_callback = None
        self._send_signal = None
        self._receive_callback = None
        self._receive_signal = None

        self._receive_queue = Queue()
        self._timeout = 10.0
        self._connection_status, self._need_recv_exit, self._need_listen_exit = Event(), Event(), Event()

    def set_ip_port(self, ip: Optional[str] = None, port: Optional[int] = None):
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port

    def set_heartbeat_timeout(self, timeout: float):
        self._timeout = timeout

    def set_closing_callback(self, callback):
        self._closing_callback = callback

    def set_closing_signal(self, signal):
        self._closing_signal = signal

    def set_connected_callback(self, callback):
        self._connected_callback = callback

    def set_connected_signal(self, signal):
        self._connected_signal = signal

    def set_disconnected_callback(self, callback):
        self._disconnected_callback = callback

    def set_disconnected_signal(self, signal):
        self._disconnected_signal = signal

    def set_send_callback(self, callback):
        self._send_callback = callback

    def set_send_signal(self, signal):
        self._send_signal = signal

    def set_receive_callback(self, callback):
        self._receive_callback = callback

    def set_receive_signal(self, signal):
        self._receive_signal = signal

    def _listen_thread(self, ip: str, port: int):
        while not self._need_listen_exit.isSet():
            if self._connection_status.isSet():
                sleep(2)
                continue
            try:
                self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self._s.bind((ip, port))
                self._s.listen(1)
                # print("connecting...")
                self.client_s, (self.client_ip, self.client_port) = self._s.accept()
                # print("connected")
                self._connection_status.set()
                self._need_recv_exit.clear()
                self._receive_th = Thread(target=self._receive_thread)
                self._receive_th.start()
                if self._connected_callback is not None:
                    self._connected_callback()
                if self._connected_signal is not None:
                    self._connected_signal.emit()
                # print("receiving...")
            except BaseException as e:
                pass
                self._close()

    def _close(self) -> None:
        try:
            self.client_s.shutdown(socket.SHUT_RDWR)
            self.client_s.close()
        except BaseException as e:
            pass
        self.client_s, self.client_ip, self.client_port = None, None, None
        self._last_heartbeat = None
        self._connection_status.clear()
        if self._disconnected_callback is not None:
            self._disconnected_callback()
        if self._disconnected_signal is not None:
            self._disconnected_signal.emit()
        self._need_recv_exit.set()

    def close(self) -> None:
        try:
            self._s.close()
        except BaseException as e:
            pass
        if self._closing_callback is not None:
            self._closing_callback()
        if self._closing_signal is not None:
            self._closing_signal.emit()
        self._close()
        self._need_recv_exit.set()
        self._need_listen_exit.set()

    def is_connected(self) -> bool:
        return self._connection_status.isSet()

    def start_listen_thread(self, ip: Optional[str] = None, port: Optional[int] = None):
        if ip is not None and port is not None:
            self.ip, self.port = ip, port
        self._listen_th = Thread(target=self._listen_thread, args=(self.ip, self.port))
        self._listen_th.start()

    def _receive_thread(self):
        while not self._need_recv_exit.isSet():
            data = None
            if not self._connection_status.isSet():
                sleep(2)
                continue
            try:
                self.client_s.settimeout(2)
                data = self.client_s.recv(1024)
            except BaseException as e:
                pass
            if self._last_heartbeat is None:
                self._last_heartbeat = time()
            if time() - self._last_heartbeat > self._timeout:
                # print(time() - self._last_heartbeat)
                # print("timeout")
                self._close()

            if data is not None and len(data) != 0:
                if self._receive_callback is not None:
                    self._receive_callback()
                if self._receive_signal is not None:
                    self._receive_signal.emit(data)
                # if data != b"\xaa\x00\x00\x00\x03hb\xff\xff\xff\xbb":
                #     self._receive_queue.put(data)
                # else:
                #     pass
                self._last_heartbeat = time()

    def send_datagram(self, datagram: bytes):
        try:
            self.client_s.settimeout(2)
            self.client_s.sendall(datagram)
            if self._send_callback is not None:
                self._send_callback(datagram)
            if self._send_signal is not None:
                self._send_signal.emit(datagram)
        except BaseException as e:
            # print(e)
            self._close()

    @classmethod
    def get_server_ip_list(cls) -> list:
        addrs = socket.getaddrinfo(socket.gethostname(), None)
        addrs = [i[4][0] for i in addrs]
        ip4_list = [i for i in addrs if
                    re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                             i) is not None]
        ip6_list = [i for i in addrs if
                    re.match(
                        r"^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$",
                        i) is not None]
        ip4_list_192 = [i for i in ip4_list if re.match(r"^192\.168\.\S*$", i) is not None]

        return ip4_list_192 + list(set(ip4_list) - set(ip4_list_192)) + ip6_list


if __name__ == '__main__':
    # s = Server()
    # s.start_listen_thread("192.168.2.125", 13452)
    Server.get_server_ip_list()

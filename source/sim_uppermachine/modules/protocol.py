from typing import Optional, Union
from crcmod import mkCrcFun
import struct


class Protocol(object):
    calc_crc16 = mkCrcFun(0x18005, rev=True, initCrc=0xffff, xorOut=0x0000)

    def __init__(self, cmd_data_bytes: Optional[bytes] = None, cmd: Union[bytes, str, None] = None,
                 data: Optional[bytes] = None, start: Union[bytes, str] = b'\xaa',
                 end: Union[bytes, str] = b'\xbb'):
        assert (cmd_data_bytes is not None and cmd is None and data is None) or (
                cmd_data_bytes is None and cmd is not None and data is not None), AssertionError(
            "choose cmd_data_bytes or cmd/data")

        if cmd is not None:
            self.cmd_bytes = cmd.encode("ascii") if isinstance(cmd, str) else cmd
            self.data_bytes = data
        else:
            self.cmd_bytes = cmd_data_bytes[:2]
            self.data_bytes = cmd_data_bytes[2:]

        self.start_bytes = start
        self.end_bytes = end
        self._calc_datagram()

    def _calc_datagram(self) -> bytes:
        self.length_bytes = struct.pack(">L", len(self.cmd_bytes) + len(self.data_bytes))
        length_cmd_data_bytes = self.length_bytes + self.cmd_bytes + self.data_bytes
        self.check_bytes = struct.pack(">H", Protocol.calc_crc16(length_cmd_data_bytes))
        self.datagram = self.start_bytes + length_cmd_data_bytes + self.check_bytes + self.end_bytes

    def get_datagram(self):
        return self.datagram

    def get_length_bytes(self) -> bytes:
        return self.length_bytes

    def get_start_bytes(self) -> bytes:
        return self.start_bytes

    def get_end_bytes(self) -> bytes:
        return self.end_bytes

    def get_command_bytes(self) -> bytes:
        return self.cmd_bytes

    def get_check_bytes(self) -> bytes:
        return self.check_bytes

    def get_data_bytes(self) -> bytes:
        return self.data_bytes

    def get_length(self) -> int:
        return len(self.cmd_bytes) + len(self.data_bytes)

    def __len__(self):
        return len(self.datagram)

    def get_data(self) -> int:
        try:
            return int(self.data_bytes.decode("ascii"))
        except BaseException as e:
            return -1

    def get_command(self) -> str:
        return self.cmd_bytes.decode("ascii")

    def print_summary(self):
        print(str(self.get_datagram()) + "\n")
        print("total bytes:", len(p))
        print("start:", self.get_start_bytes())
        print("length:", self.get_length())
        print("command:", self.get_command())
        print("data:", p.get_data())
        print("check:", p.get_check_bytes())
        print("end:", p.get_end_bytes())



if __name__ == '__main__':
    p = Protocol(cmd_data_bytes=b'st\xff')
    p.print_summary()
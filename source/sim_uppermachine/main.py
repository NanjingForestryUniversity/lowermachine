"""
BY: Miaow, Wanderson M.Pimenta
PROJECT MADE WITH: Qt Designer and PySide6
V: 1.0.0

This project can be used freely for all uses, as long as they maintain the
respective credits only in the Python scripts, any information in the visual
interface (GUI) can be modified without any implication.

There are limitations on Qt licenses if you want to use your products
commercially, I recommend reading them on the official website:
https://doc.qt.io/qtforpython/licenses.html
"""
import re
import sys
import os
import time
from threading import Thread, Event
from binascii import unhexlify, hexlify
from typing import Optional
import json
import PySide6

from modules.list_model import PacketListModel
from modules.protocol import Protocol

from PySide6.QtCore import Signal

from modules import *
from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox, QLineEdit, QSpinBox
from PySide6.QtGui import QIcon, QFontMetrics, QStandardItemModel, QStandardItem
from modules.ui_main import Ui_MainWindow
from modules.server import Server


# os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

class MainWindow(QMainWindow):
    connected_signal = Signal()
    disconnected_signal = Signal()
    send_signal = Signal(bytes)
    receive_signal = Signal(bytes)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.packet_list_model = QStandardItemModel()
        with open("settings.json") as f:
            self.settings = json.load(f)
        UIFunctions.uiDefinitions(self)  # set ui, e.g. title bar, grip & resize, min/max/close

        self.total_send_bytes, self.total_send_packets = 0, 0
        self.total_receive_bytes, self.total_receive_packets = 0, 0

        # ===buttons on left menu bar===
        self.ui.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        self.ui.btn_home.clicked.connect(self.menu_btn_clicked)
        self.ui.btn_connection.clicked.connect(self.menu_btn_clicked)
        self.ui.btn_divider.clicked.connect(self.menu_btn_clicked)
        self.ui.btn_valvedata.clicked.connect(self.menu_btn_clicked)

        # set custom theme
        # UIFunctions.theme(self, "themes\py_dracula_light.qss", True)
        # AppFunctions.setThemeHack(self)

        # ===page_connection===
        page_connection_settings = self.settings["page_connection"]
        self.ui.sb_server_port.setValue(page_connection_settings["server_port"])

        # ===page_divider===
        page_divider_settings = self.settings["page_divider"]
        [self.ui.__dict__[f"pb_send_{i}"].clicked.connect(self.pb_send_clicked) for i in range(1, 6)]
        for t in ["start", "command", "data", "end"]:
            for i in range(1, 6):
                cb = self.ui.__dict__[f"cb_{t}_{i}"]
                cb.currentTextChanged.connect(self.manual_current_text_changed)
                cb.clear()
                cb.addItems(page_divider_settings["manual"][f"cb_{t}_list"])
                cb.setCurrentText(page_divider_settings["manual"]["data"][i][f"cb_{t}"])

        [self.ui.__dict__[f"pb_send_camera_{t}"].clicked.connect(self.pb_send_camera_clicked) for t in "abcd"]
        self.ui.le_preset_num.textChanged.connect(self.le_preset_num_text_changed)
        self.ui.le_preset_num.setText(str(page_divider_settings["preset"]["le_preset_num"]))
        self.ui.btn_preset_next.clicked.connect(self.btn_preset_next_clicked)
        self.ui.btn_preset_previous.clicked.connect(self.btn_preset_previous_clicked)
        self.ui.btn_preset_add.clicked.connect(self.btn_preset_add_clicked)

        self.ui.pb_send_camera_all.clicked.connect(self.pb_send_camera_all_clicked)
        self.ui.pb_send_start.clicked.connect(self.pb_send_start_clicked)
        self.ui.pb_send_stop.clicked.connect(self.pb_send_stop_clicked)
        self.ui.pb_divider_restore.clicked.connect(self.pb_divider_restore_clicked)

        # ===show main window, start at page_home page with stopped status===
        self.show()
        self.ui.btn_home.click()
        self.connected_signal.connect(self.slot_connected_signal)
        self.disconnected_signal.connect(self.slot_disconnected_signal)
        self.send_signal.connect(self.slot_send_signal)
        self.receive_signal.connect(self.slot_receive_signal)
        self.server: Optional[Server] = None
        self.init_server()

    def init_server(self):
        if self.server is not None:
            self.server.close()
        self.server = Server()
        self.server.set_connected_signal(self.connected_signal)
        self.server.set_disconnected_signal(self.disconnected_signal)
        self.server.set_send_signal(self.send_signal)
        self.server.set_receive_signal(self.receive_signal)
        last_selected = self.ui.cb_server_ip.currentText()
        self.ui.cb_server_ip.clear()
        ip_list = Server.get_server_ip_list()
        self.ui.cb_server_ip.addItems(ip_list)
        if last_selected is not None and last_selected.strip() != "" and last_selected in ip_list:
            self.ui.cb_server_ip.setCurrentText(last_selected)
        else:
            self.ui.cb_server_ip.setCurrentIndex(0)

    def slot_send_signal(self, data: bytes):
        self.total_send_bytes += len(data)
        self.total_send_packets += 1
        self.ui.lbl_tx_count.setText(f"{self.total_send_bytes} bytes | {self.total_send_packets} packets")
        data = hexlify(data, " ").decode("ascii").upper()
        UIFunctions.set_elide_text(self.ui.lbl_datagram, data)
        item = QStandardItem(data)
        item.setIcon(QIcon(u":/icons/images/icons/cil-cloud-upload-small.png"))
        self.packet_list_model.appendRow(item)

    def slot_receive_signal(self, data: bytes):
        self.total_receive_bytes += len(data)
        self.total_receive_packets += 1
        self.ui.lbl_rx_count.setText(f"{self.total_receive_bytes} bytes | {self.total_receive_packets} packets")
        if data != b"\xaa\x00\x00\x00\x03hb\xff\xff\xff\xbb":
            data = hexlify(data, " ").decode("ascii").upper()
            UIFunctions.set_elide_text(self.ui.lbl_datagram, data)
            item = QStandardItem(data)
            item.setIcon(QIcon(u":/icons/images/icons/cil-cloud-download-small.png"))
            self.packet_list_model.appendRow(item)

    def slot_connected_signal(self):
        self.ui.page_divider.setEnabled(True)
        self.ui.lbl_server_addr.setText(f"{self.server.ip}:{self.server.port}")
        self.ui.lbl_client_addr.setText(f"{self.server.client_ip}:{self.server.client_port}")
        self.ui.lv_packets.setModel(self.packet_list_model)

    def slot_disconnected_signal(self):
        self.ui.page_divider.setEnabled(False)
        self.ui.lbl_server_addr.setText(f"0.0.0.0:0")
        self.ui.lbl_client_addr.setText(f"0.0.0.0:0")

    def menu_btn_clicked(self):
        btn = self.sender()
        btnName = btn.objectName()

        # show page_home page
        if btnName == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # show settings page
        if btnName == "btn_connection":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_connection)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # transmission page
        if btnName == "btn_divider":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_divider)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            if self.server.ip is None or self.server.ip != self.ui.cb_server_ip.currentText() or self.server.port != self.ui.sb_server_port.value():
                self.init_server()
                self.server.start_listen_thread(self.ui.cb_server_ip.currentText(), self.ui.sb_server_port.value())

        # show table page
        if btnName == "btn_valvedata":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_valvedata)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    def pb_send_clicked(self):
        try:
            index = int(self.sender().objectName()[-1])
            cb_start: QComboBox = self.ui.__dict__[f"cb_start_{index}"]
            cb_command: QComboBox = self.ui.__dict__[f"cb_command_{index}"]
            cb_data: QComboBox = self.ui.__dict__[f"cb_data_{index}"]
            cb_end: QComboBox = self.ui.__dict__[f"cb_end_{index}"]
            start = unhexlify(cb_start.currentText().replace(" ", ""))
            command = cb_command.currentText().replace(" ", "").encode("ascii").lower()
            data = unhexlify(cb_data.currentText().replace(" ", ""))
            end = unhexlify(cb_end.currentText().replace(" ", ""))

            p = Protocol(start=start, cmd=command, data=data, end=end)
            self.server.send_datagram(p.get_datagram())

        except BaseException as e:
            pass

    def pb_divider_restore_clicked(self):
        self.ui.le_preset_num.setText("1")

    def pb_send_camera_clicked(self):
        try:
            abcd = self.sender().objectName()[-1]
            sb_camera: QSpinBox = self.ui.__dict__[f"sb_camera_{abcd}"]
            data = sb_camera.value()
            p = Protocol(cmd=f"p{abcd}", data=f"{data:08d}".encode("ascii"))
            self.server.send_datagram(p.get_datagram())
        except BaseException as e:
            pass

    def manual_current_text_changed(self):
        try:
            index = int(self.sender().objectName()[-1])
            cb_start: QComboBox = self.ui.__dict__[f"cb_start_{index}"]
            cb_command: QComboBox = self.ui.__dict__[f"cb_command_{index}"]
            cb_data: QComboBox = self.ui.__dict__[f"cb_data_{index}"]
            cb_end: QComboBox = self.ui.__dict__[f"cb_end_{index}"]
            start = unhexlify(cb_start.currentText().replace(" ", ""))
            command = cb_command.currentText().replace(" ", "").encode("ascii").lower()
            data = unhexlify(cb_data.currentText().replace(" ", ""))
            end = unhexlify(cb_end.currentText().replace(" ", ""))

            p = Protocol(start=start, cmd=command, data=data, end=end)
            le_length: QLineEdit = self.ui.__dict__[f"le_length_{index}"]
            le_check: QLineEdit = self.ui.__dict__[f"le_check_{index}"]
            le_length.setText(str(p.get_length()))
            le_check.setText(hexlify(p.get_check_bytes(), " ").decode("ascii"))
        except BaseException as e:
            le_length: QLineEdit = self.ui.__dict__[f"le_length_{index}"]
            le_check: QLineEdit = self.ui.__dict__[f"le_check_{index}"]
            le_length.setText("--")
            le_check.setText("--")

    def le_preset_num_text_changed(self):
        index = int(self.ui.le_preset_num.text())
        data = self.settings["page_divider"]["preset"]["data"][index - 1]
        self.ui.le_preset_name.setText(data["le_preset_name"])
        [self.ui.__dict__[f"sb_camera_{t}"].setValue(data[f"sb_camera_{t}"]) for t in "abcd"]
        self.ui.sb_valve.setValue(data["sb_valve"])
        self.ui.cb_from_camera.setCurrentText(data["cb_from_camera"])
        self.ui.le_to_valve.setText(str(data["le_to_valve"]))
        length = len(self.settings["page_divider"]["preset"]["data"])
        self.ui.btn_preset_next.setEnabled(index != length)
        self.ui.btn_preset_previous.setEnabled(index != 1)

    def btn_preset_next_clicked(self):
        last_index = int(self.ui.le_preset_num.text())
        length = len(self.settings["page_divider"]["preset"]["data"])
        if last_index < length:
            last_index += 1
            self.ui.le_preset_num.setText(str(last_index))

    def btn_preset_previous_clicked(self):
        last_index = int(self.ui.le_preset_num.text())
        if last_index > 1:
            last_index -= 1
            self.ui.le_preset_num.setText(str(last_index))

    def btn_preset_add_clicked(self):
        data = self.settings["page_divider"]["preset"]["data"]
        tmp_name = self.ui.le_preset_name.text()
        tmp_name_adj = tmp_name.replace("(", r"\(").replace(")", r"\)")

        num_list = []
        for i in data:
            l = re.findall(rf"^{tmp_name_adj}\s\((\d+)\)$", i["le_preset_name"])
            if len(l) != 0:
                num_list.append(int(l[-1]))
        if len(num_list) != 0:
            tmp_name += f" ({max(num_list) + 1})"
        for i in data:
            if tmp_name == i["le_preset_name"]:
                tmp_name += " (1)"
                break

        new_dict = {
            "le_preset_name": tmp_name,
            "sb_camera_a": self.ui.sb_camera_a.value(),
            "sb_camera_b": self.ui.sb_camera_b.value(),
            "sb_camera_c": self.ui.sb_camera_c.value(),
            "sb_camera_d": self.ui.sb_camera_d.value(),
            "sb_valve": self.ui.sb_valve.value(),
            "cb_from_camera": self.ui.cb_from_camera.currentText(),
            "le_to_valve": int(self.ui.le_to_valve.text())
        }
        data.append(new_dict)
        length = len(data)
        self.ui.le_preset_name.setText(tmp_name)
        self.ui.le_preset_num.setText(str(length))

    def pb_send_camera_all_clicked(self):
        try:
            [self.server.send_datagram(Protocol(cmd=f"p{abcd}",
                                                data=f"{self.ui.__dict__[f'sb_camera_{abcd}'].value():08d}".encode(
                                                    "ascii")).get_datagram()) for abcd in "abcd"]
        except BaseException as e:
            pass

    def pb_send_start_clicked(self):
        try:
            p = Protocol(cmd=b"st", data=b"\xff")
            self.server.send_datagram(p.get_datagram())
        except BaseException as e:
            pass

    def pb_send_stop_clicked(self):
        try:
            p = Protocol(cmd=b"sp", data=b"\xff")
            self.server.send_datagram(p.get_datagram())
        except BaseException as e:
            pass

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        super().closeEvent(event)
        self.server.close()
        with open(self.ui.le_profile_file.text(), "w") as f:
            json.dump(self.settings, f)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())

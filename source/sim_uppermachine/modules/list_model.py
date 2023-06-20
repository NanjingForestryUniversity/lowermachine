from binascii import hexlify
from typing import List

from PySide6.QtCore import QAbstractListModel, Qt


class PacketListModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = []

    def rowCount(self, parent):
        return len(self._data)

    def append(self, obj):
        self._data.append(obj)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()]
        else:
            return None

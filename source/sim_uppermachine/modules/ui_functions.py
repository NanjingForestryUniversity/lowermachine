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
from typing import List

from main import MainWindow
from PySide6.QtCore import (Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup,
                            QEvent, QTimer)
from PySide6.QtGui import QIcon, QColor, QFontMetrics
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QPushButton, QComboBox, QWidget
from modules.app_settings import Settings
from widgets.custom_grips.custom_grips import CustomGrip

GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True


class UIFunctions(MainWindow):

    def maximize_restore(self):
        """
        MAXIMIZE/RESTORE
        """
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    def returStatus(self):
        """
        RETURN STATUS
        """
        return GLOBAL_STATE

    def setStatus(self, status):
        """
        SET STATUS
        """
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def toggleMenu(self, enable):
        """
        TOGGLE MENU
        """
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        # self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    def selectMenu(getStyle):
        """
        SELECT/DESELECT MENU
        """
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    def deselectMenu(getStyle):
        """
        SELECT/DESELECT MENU
        :return:
        """
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    def selectStandardMenu(self, widget):
        """
        START SELECTION
        """
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    def resetStyle(self, widget):
        """
        RESET SELECTION
        """
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    def theme(self, file, useCustomTheme):
        """
        IMPORT THEMES FILES QSS/CSS
        """
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    def uiDefinitions(self):
        """
        GUI DEFINITIONS
        """

        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            # STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
                    self.drag_pos = event.globalPosition().toPoint()
                    event.accept()

            def mousePressEvent(event):
                self.drag_pos = event.globalPosition().toPoint()

            self.ui.titleRightInfo.mouseMoveEvent = moveWindow
            self.ui.leftMenuBg.mouseMoveEvent = moveWindow
            self.mousePressEvent = mousePressEvent

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        def resize_grips(event):
            if Settings.ENABLE_CUSTOM_TITLE_BAR:
                self.left_grip.setGeometry(0, 10, 10, self.height())
                self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
                self.top_grip.setGeometry(0, 0, self.width(), 10)
                self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")
        self.resizeEvent = resize_grips

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(self.close)
        self.ui.btn_exit.clicked.connect(self.close)

        # COMBOBOX STYLE HACK
        box_list: List[QComboBox] = self.ui.styleSheet.findChildren(QComboBox, options=Qt.FindChildrenRecursively)
        for box in box_list:
            w = box.view().window()
            w.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
            w.setAttribute(Qt.WA_TranslucentBackground)
            w.setStyleSheet(f"QComboBox QAbstractItemView:item{{height:{w.height()};}}")

        self.ui.cb_start_list = [self.ui.__dict__[f"cb_start_{i}"] for i in range(1, 6)]
        self.ui.le_length_list = [self.ui.__dict__[f"le_length_{i}"] for i in range(1, 6)]
        self.ui.cb_command_list = [self.ui.__dict__[f"cb_command_{i}"] for i in range(1, 6)]
        self.ui.cb_data_list = [self.ui.__dict__[f"cb_data_{i}"] for i in range(1, 6)]
        self.ui.le_check_list = [self.ui.__dict__[f"le_check_{i}"] for i in range(1, 6)]
        self.ui.cb_end_list = [self.ui.__dict__[f"cb_end_{i}"] for i in range(1, 6)]
        self.ui.pb_preset_list = [self.ui.__dict__[f"pb_preset_{i}"] for i in range(1, 6)]
        self.ui.pb_send_list = [self.ui.__dict__[f"pb_send_{i}"] for i in range(1, 6)]

    @classmethod
    def set_elide_text(cls, widget: QWidget, text: str):
        elided_text = widget.fontMetrics().elidedText(text, Qt.ElideMiddle, widget.width() - 20)
        widget.setText(elided_text)

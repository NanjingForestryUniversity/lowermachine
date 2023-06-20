# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)
from modules import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 650)
        MainWindow.setMinimumSize(QSize(950, 650))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Bg App */\n"
"#bgApp {	\n"
"	background-color: rg"
                        "b(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"/* #titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); } */\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #ff79c6; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-origin: padding;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-co"
                        "lor: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#topMenu .QLabel {\n"
"    border-top: 1px solid rgba(255, 255, 255, 50); /*rgb(113, 126, 149);*/\n"
"    margin: 15px 10px;\n"
"	height: 2px;\n"
"	min-height: 2px;\n"
"	max-height: 2px;\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	bo"
                        "rder-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#e"
                        "xtraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 38px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBot"
                        "tom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 5px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
""
                        "}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////QTableView */\n"
"QTableView {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	padding: 0px;\n"
"}\n"
"QTableView::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableView::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"    text-ali"
                        "gn: center;\n"
"}\n"
"QTableView::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3p, 0px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView .QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 9px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QHeaderView .QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 9px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView .QScrollBar::handle:horizontal {\n"
"	border-radius: 3.5px;\n"
"}\n"
"QHeaderView .QScrollBar:vertical {\n"
"	border-radius: 3.5px;\n"
" }\n"
"QTableView ."
                        "QTableCornerButton::section {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 5px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"SpinBox */\n"
"QSpinBox {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 5px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71"
                        ", 88);\n"
"}\n"
"QSpinBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"} \n"
"QSpinBox::up-button { \n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top left;\n"
"	background-color: rgb(33, 37, 43);\n"
"	width: 25px; \n"
"	margin: 0px;\n"
"	border: none;\n"
"	border-right: 3px solid rgba(39, 44, 54, 150) ; \n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;	\n"
"}\n"
"QSpinBox::up-button:pressed  { \n"
"	background-color: rgba(39, 44, 54, 150);\n"
"}\n"
"QSpinBox::up-arrow {\n"
"	image: url(:/icons/images/icons/chevron-miniup.png);\n"
"}\n"
"QSpinBox::down-button { \n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom left;\n"
"	background-color: rgb(33, 37, 43);\n"
"	width: 25px; \n"
"	margin: 0px;\n"
"	border: none;\n"
"	border-right: 3px solid rgba(39, 44, 54, 150) ; \n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;	\n"
"}\n"
"QSpinBox::down-button:pressed  { \n"
"	background-color: rgba(39, 44, 54, 150);\n"
"}\n"
"QSpinBox::down-arr"
                        "ow { \n"
"	image: url(:/icons/images/icons/chevron-minidown.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:hor"
                        "izontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
""
                        " }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheck"
                        "Box::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////"
                        "////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(33, 37, 43);\n"
"	/*background-color: rgb(27, 29, 35);*/\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"} \n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
" }\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/images/icons/chevron-down.png);\n"
"}\n"
"QComboBox::drop-down:pressed {\n"
"	background-color: rgba(39, 44, 54, 150);\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	outline: 0px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
""
                        "	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	selection-background-color: rgb(52, 59, 72);\n"
"	margin-top: 5px;\n"
"/*\n"
"	padding-top:5px;\n"
"	padding-bottom:5px;\n"
"*/\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"	border-radius: 5px;\n"
"	height: 25px;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    color:rgb(255,255,255);\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    marg"
                        "in: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
""
                        "	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ListView */\n"
"QListView {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	outline: none;\n"
"	alternate-background-color:yellow;\n"
"}\n"
"QListView::item {\n"
"	height: 30px;\n"
"	border-radius: 5px;\n"
"}\n"
"QListView::item:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QListView::item:selected {\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"TextEdit */\n"
"QTextEdit {\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"\n"
"#pagesContainer QPushButton {\n"
"	margin: 0px;\n"
"    background-origin: content;\n"
"    background-position: left;\n"
"    background-repeat: no-repeat;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* "
                        "/////////////////////////////////////////////////////////////////////////////////////////////////\n"
"StackedWidget */\n"
"\n"
"#page_home, #page_connection, #page_divider, #page_valvedata {\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 50))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 50))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_connection = QPushButton(self.topMenu)
        self.btn_connection.setObjectName(u"btn_connection")
        self.btn_connection.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_connection.sizePolicy().hasHeightForWidth())
        self.btn_connection.setSizePolicy(sizePolicy)
        self.btn_connection.setMinimumSize(QSize(0, 50))
        self.btn_connection.setFont(font)
        self.btn_connection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connection.setLayoutDirection(Qt.LeftToRight)
        self.btn_connection.setStyleSheet(u"background-image: url(:/icons/images/icons/sliders.png);")

        self.verticalLayout_8.addWidget(self.btn_connection)

        self.btn_divider = QPushButton(self.topMenu)
        self.btn_divider.setObjectName(u"btn_divider")
        sizePolicy.setHeightForWidth(self.btn_divider.sizePolicy().hasHeightForWidth())
        self.btn_divider.setSizePolicy(sizePolicy)
        self.btn_divider.setMinimumSize(QSize(0, 50))
        self.btn_divider.setFont(font)
        self.btn_divider.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_divider.setLayoutDirection(Qt.LeftToRight)
        self.btn_divider.setStyleSheet(u"background-image: url(:/icons/images/icons/aperture.png);")

        self.verticalLayout_8.addWidget(self.btn_divider)

        self.btn_valvedata = QPushButton(self.topMenu)
        self.btn_valvedata.setObjectName(u"btn_valvedata")
        self.btn_valvedata.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_valvedata.sizePolicy().hasHeightForWidth())
        self.btn_valvedata.setSizePolicy(sizePolicy)
        self.btn_valvedata.setMinimumSize(QSize(0, 50))
        self.btn_valvedata.setFont(font)
        self.btn_valvedata.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_valvedata.setLayoutDirection(Qt.LeftToRight)
        self.btn_valvedata.setStyleSheet(u"background-image: url(:/icons/images/icons/image.png);")

        self.verticalLayout_8.addWidget(self.btn_valvedata)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_exit = QPushButton(self.bottomMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 50))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/log-out.png);")

        self.verticalLayout_9.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 0, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.page_home)
        self.page_connection = QWidget()
        self.page_connection.setObjectName(u"page_connection")
        self.page_connection.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.page_connection)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 5, 10, 10)
        self.row_1 = QFrame(self.page_connection)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_content_wid_1)
        self.verticalLayout_28.setSpacing(3)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.le_profile_file = QLineEdit(self.frame_content_wid_1)
        self.le_profile_file.setObjectName(u"le_profile_file")
        self.le_profile_file.setMinimumSize(QSize(0, 30))
        self.le_profile_file.setStyleSheet(u"")
        self.le_profile_file.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.le_profile_file)

        self.pb_load_profile = QPushButton(self.frame_content_wid_1)
        self.pb_load_profile.setObjectName(u"pb_load_profile")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pb_load_profile.sizePolicy().hasHeightForWidth())
        self.pb_load_profile.setSizePolicy(sizePolicy3)
        self.pb_load_profile.setMinimumSize(QSize(75, 30))
        self.pb_load_profile.setFont(font)
        self.pb_load_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_load_profile.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_load_profile.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.pb_load_profile)

        self.pb_save_profile = QPushButton(self.frame_content_wid_1)
        self.pb_save_profile.setObjectName(u"pb_save_profile")
        sizePolicy3.setHeightForWidth(self.pb_save_profile.sizePolicy().hasHeightForWidth())
        self.pb_save_profile.setSizePolicy(sizePolicy3)
        self.pb_save_profile.setMinimumSize(QSize(75, 30))
        self.pb_save_profile.setFont(font)
        self.pb_save_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_save_profile.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_save_profile.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.pb_save_profile)


        self.verticalLayout_28.addLayout(self.horizontalLayout_9)

        self.labelVersion_4 = QLabel(self.frame_content_wid_1)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        sizePolicy3.setHeightForWidth(self.labelVersion_4.sizePolicy().hasHeightForWidth())
        self.labelVersion_4.setSizePolicy(sizePolicy3)
        self.labelVersion_4.setMinimumSize(QSize(0, 15))
        self.labelVersion_4.setMaximumSize(QSize(16777215, 15))
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.labelVersion_4)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.frame_title_wid_2 = QFrame(self.page_connection)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.labelBoxBlenderInstalation_3)


        self.verticalLayout.addWidget(self.frame_title_wid_2)

        self.row_2 = QFrame(self.page_connection)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.row_2)
        self.horizontalLayout_10.setSpacing(25)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.lbl_server_ip = QLabel(self.row_2)
        self.lbl_server_ip.setObjectName(u"lbl_server_ip")
        sizePolicy3.setHeightForWidth(self.lbl_server_ip.sizePolicy().hasHeightForWidth())
        self.lbl_server_ip.setSizePolicy(sizePolicy3)
        self.lbl_server_ip.setMinimumSize(QSize(0, 26))
        self.lbl_server_ip.setMaximumSize(QSize(16777215, 26))
        self.lbl_server_ip.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_server_ip.setLineWidth(1)
        self.lbl_server_ip.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.lbl_server_ip)

        self.cb_server_ip = QComboBox(self.row_2)
        self.cb_server_ip.setObjectName(u"cb_server_ip")
        self.cb_server_ip.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.cb_server_ip.sizePolicy().hasHeightForWidth())
        self.cb_server_ip.setSizePolicy(sizePolicy3)
        self.cb_server_ip.setMinimumSize(QSize(0, 34))
        self.cb_server_ip.setMaximumSize(QSize(16777215, 34))
        self.cb_server_ip.setFont(font)
        self.cb_server_ip.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_server_ip.setStyleSheet(u"")
        self.cb_server_ip.setIconSize(QSize(16, 16))

        self.verticalLayout_26.addWidget(self.cb_server_ip)

        self.lbl_server_port = QLabel(self.row_2)
        self.lbl_server_port.setObjectName(u"lbl_server_port")
        sizePolicy3.setHeightForWidth(self.lbl_server_port.sizePolicy().hasHeightForWidth())
        self.lbl_server_port.setSizePolicy(sizePolicy3)
        self.lbl_server_port.setMinimumSize(QSize(0, 26))
        self.lbl_server_port.setMaximumSize(QSize(16777215, 26))
        self.lbl_server_port.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lbl_server_port.setLineWidth(1)
        self.lbl_server_port.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.lbl_server_port)

        self.sb_server_port = QSpinBox(self.row_2)
        self.sb_server_port.setObjectName(u"sb_server_port")
        self.sb_server_port.setMinimumSize(QSize(0, 34))
        self.sb_server_port.setMinimum(1)
        self.sb_server_port.setMaximum(65535)
        self.sb_server_port.setValue(13452)

        self.verticalLayout_26.addWidget(self.sb_server_port)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_26)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)

        self.verticalLayout.addWidget(self.row_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_connection)
        self.page_divider = QWidget()
        self.page_divider.setObjectName(u"page_divider")
        self.page_divider.setEnabled(False)
        self.horizontalLayout_11 = QHBoxLayout(self.page_divider)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelBoxBlenderInstalation_4 = QLabel(self.page_divider)
        self.labelBoxBlenderInstalation_4.setObjectName(u"labelBoxBlenderInstalation_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelBoxBlenderInstalation_4.sizePolicy().hasHeightForWidth())
        self.labelBoxBlenderInstalation_4.setSizePolicy(sizePolicy4)
        self.labelBoxBlenderInstalation_4.setFont(font)
        self.labelBoxBlenderInstalation_4.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.labelBoxBlenderInstalation_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cb_end_3 = QComboBox(self.page_divider)
        self.cb_end_3.addItem("")
        self.cb_end_3.setObjectName(u"cb_end_3")
        sizePolicy3.setHeightForWidth(self.cb_end_3.sizePolicy().hasHeightForWidth())
        self.cb_end_3.setSizePolicy(sizePolicy3)
        self.cb_end_3.setMinimumSize(QSize(64, 30))
        self.cb_end_3.setMaximumSize(QSize(70, 30))
        self.cb_end_3.setEditable(True)

        self.gridLayout.addWidget(self.cb_end_3, 3, 5, 1, 1)

        self.cb_data_5 = QComboBox(self.page_divider)
        self.cb_data_5.addItem("")
        self.cb_data_5.setObjectName(u"cb_data_5")
        sizePolicy.setHeightForWidth(self.cb_data_5.sizePolicy().hasHeightForWidth())
        self.cb_data_5.setSizePolicy(sizePolicy)
        self.cb_data_5.setMinimumSize(QSize(55, 30))
        self.cb_data_5.setMaximumSize(QSize(16777215, 30))
        self.cb_data_5.setEditable(True)

        self.gridLayout.addWidget(self.cb_data_5, 5, 3, 1, 1)

        self.lbl_data = QLabel(self.page_divider)
        self.lbl_data.setObjectName(u"lbl_data")
        sizePolicy3.setHeightForWidth(self.lbl_data.sizePolicy().hasHeightForWidth())
        self.lbl_data.setSizePolicy(sizePolicy3)
        self.lbl_data.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout.addWidget(self.lbl_data, 0, 3, 1, 1)

        self.le_check_4 = QLineEdit(self.page_divider)
        self.le_check_4.setObjectName(u"le_check_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.le_check_4.sizePolicy().hasHeightForWidth())
        self.le_check_4.setSizePolicy(sizePolicy5)
        self.le_check_4.setMinimumSize(QSize(55, 30))
        self.le_check_4.setMaximumSize(QSize(50, 30))
        self.le_check_4.setReadOnly(True)

        self.gridLayout.addWidget(self.le_check_4, 4, 4, 1, 1)

        self.lbl_start = QLabel(self.page_divider)
        self.lbl_start.setObjectName(u"lbl_start")
        sizePolicy3.setHeightForWidth(self.lbl_start.sizePolicy().hasHeightForWidth())
        self.lbl_start.setSizePolicy(sizePolicy3)
        self.lbl_start.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout.addWidget(self.lbl_start, 0, 0, 1, 1)

        self.cb_start_3 = QComboBox(self.page_divider)
        self.cb_start_3.addItem("")
        self.cb_start_3.setObjectName(u"cb_start_3")
        sizePolicy5.setHeightForWidth(self.cb_start_3.sizePolicy().hasHeightForWidth())
        self.cb_start_3.setSizePolicy(sizePolicy5)
        self.cb_start_3.setMinimumSize(QSize(64, 30))
        self.cb_start_3.setMaximumSize(QSize(70, 30))
        self.cb_start_3.setEditable(True)

        self.gridLayout.addWidget(self.cb_start_3, 3, 0, 1, 1)

        self.pb_preset_2 = QPushButton(self.page_divider)
        self.pb_preset_2.setObjectName(u"pb_preset_2")
        sizePolicy4.setHeightForWidth(self.pb_preset_2.sizePolicy().hasHeightForWidth())
        self.pb_preset_2.setSizePolicy(sizePolicy4)
        self.pb_preset_2.setMinimumSize(QSize(25, 30))
        self.pb_preset_2.setMaximumSize(QSize(25, 30))
        self.pb_preset_2.setFont(font)
        self.pb_preset_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_preset_2.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/plus.png);\n"
"	background-position: center center;\n"
"}")

        self.gridLayout.addWidget(self.pb_preset_2, 2, 6, 1, 1)

        self.cb_start_2 = QComboBox(self.page_divider)
        self.cb_start_2.addItem("")
        self.cb_start_2.setObjectName(u"cb_start_2")
        sizePolicy5.setHeightForWidth(self.cb_start_2.sizePolicy().hasHeightForWidth())
        self.cb_start_2.setSizePolicy(sizePolicy5)
        self.cb_start_2.setMinimumSize(QSize(64, 30))
        self.cb_start_2.setMaximumSize(QSize(70, 30))
        self.cb_start_2.setEditable(True)

        self.gridLayout.addWidget(self.cb_start_2, 2, 0, 1, 1)

        self.lbl_check = QLabel(self.page_divider)
        self.lbl_check.setObjectName(u"lbl_check")
        sizePolicy3.setHeightForWidth(self.lbl_check.sizePolicy().hasHeightForWidth())
        self.lbl_check.setSizePolicy(sizePolicy3)
        self.lbl_check.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout.addWidget(self.lbl_check, 0, 4, 1, 1)

        self.le_length_2 = QLineEdit(self.page_divider)
        self.le_length_2.setObjectName(u"le_length_2")
        sizePolicy5.setHeightForWidth(self.le_length_2.sizePolicy().hasHeightForWidth())
        self.le_length_2.setSizePolicy(sizePolicy5)
        self.le_length_2.setMinimumSize(QSize(55, 30))
        self.le_length_2.setMaximumSize(QSize(50, 30))
        self.le_length_2.setReadOnly(True)

        self.gridLayout.addWidget(self.le_length_2, 2, 1, 1, 1)

        self.cb_end_1 = QComboBox(self.page_divider)
        self.cb_end_1.addItem("")
        self.cb_end_1.setObjectName(u"cb_end_1")
        sizePolicy3.setHeightForWidth(self.cb_end_1.sizePolicy().hasHeightForWidth())
        self.cb_end_1.setSizePolicy(sizePolicy3)
        self.cb_end_1.setMinimumSize(QSize(64, 30))
        self.cb_end_1.setMaximumSize(QSize(70, 30))
        self.cb_end_1.setEditable(True)

        self.gridLayout.addWidget(self.cb_end_1, 1, 5, 1, 1)

        self.cb_data_2 = QComboBox(self.page_divider)
        self.cb_data_2.addItem("")
        self.cb_data_2.setObjectName(u"cb_data_2")
        sizePolicy.setHeightForWidth(self.cb_data_2.sizePolicy().hasHeightForWidth())
        self.cb_data_2.setSizePolicy(sizePolicy)
        self.cb_data_2.setMinimumSize(QSize(55, 30))
        self.cb_data_2.setMaximumSize(QSize(16777215, 30))
        self.cb_data_2.setEditable(True)

        self.gridLayout.addWidget(self.cb_data_2, 2, 3, 1, 1)

        self.le_check_5 = QLineEdit(self.page_divider)
        self.le_check_5.setObjectName(u"le_check_5")
        sizePolicy5.setHeightForWidth(self.le_check_5.sizePolicy().hasHeightForWidth())
        self.le_check_5.setSizePolicy(sizePolicy5)
        self.le_check_5.setMinimumSize(QSize(55, 30))
        self.le_check_5.setMaximumSize(QSize(50, 30))
        self.le_check_5.setReadOnly(True)

        self.gridLayout.addWidget(self.le_check_5, 5, 4, 1, 1)

        self.pb_send_4 = QPushButton(self.page_divider)
        self.pb_send_4.setObjectName(u"pb_send_4")
        sizePolicy4.setHeightForWidth(self.pb_send_4.sizePolicy().hasHeightForWidth())
        self.pb_send_4.setSizePolicy(sizePolicy4)
        self.pb_send_4.setMinimumSize(QSize(25, 30))
        self.pb_send_4.setMaximumSize(QSize(25, 30))
        self.pb_send_4.setFont(font)
        self.pb_send_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_4.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/arrow-right.png);\n"
"	background-position: center center;\n"
"	border-style: none;\n"
"}")

        self.gridLayout.addWidget(self.pb_send_4, 4, 7, 1, 1)

        self.pb_send_5 = QPushButton(self.page_divider)
        self.pb_send_5.setObjectName(u"pb_send_5")
        sizePolicy4.setHeightForWidth(self.pb_send_5.sizePolicy().hasHeightForWidth())
        self.pb_send_5.setSizePolicy(sizePolicy4)
        self.pb_send_5.setMinimumSize(QSize(25, 30))
        self.pb_send_5.setMaximumSize(QSize(25, 30))
        self.pb_send_5.setFont(font)
        self.pb_send_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_5.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/arrow-right.png);\n"
"	background-position: center center;\n"
"	border-style: none;\n"
"}")

        self.gridLayout.addWidget(self.pb_send_5, 5, 7, 1, 1)

        self.pb_preset_3 = QPushButton(self.page_divider)
        self.pb_preset_3.setObjectName(u"pb_preset_3")
        sizePolicy4.setHeightForWidth(self.pb_preset_3.sizePolicy().hasHeightForWidth())
        self.pb_preset_3.setSizePolicy(sizePolicy4)
        self.pb_preset_3.setMinimumSize(QSize(25, 30))
        self.pb_preset_3.setMaximumSize(QSize(25, 30))
        self.pb_preset_3.setFont(font)
        self.pb_preset_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_preset_3.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/plus.png);\n"
"	background-position: center center;\n"
"}")

        self.gridLayout.addWidget(self.pb_preset_3, 3, 6, 1, 1)

        self.le_length_3 = QLineEdit(self.page_divider)
        self.le_length_3.setObjectName(u"le_length_3")
        sizePolicy5.setHeightForWidth(self.le_length_3.sizePolicy().hasHeightForWidth())
        self.le_length_3.setSizePolicy(sizePolicy5)
        self.le_length_3.setMinimumSize(QSize(55, 30))
        self.le_length_3.setMaximumSize(QSize(50, 30))
        self.le_length_3.setReadOnly(True)

        self.gridLayout.addWidget(self.le_length_3, 3, 1, 1, 1)

        self.cb_end_2 = QComboBox(self.page_divider)
        self.cb_end_2.addItem("")
        self.cb_end_2.setObjectName(u"cb_end_2")
        sizePolicy3.setHeightForWidth(self.cb_end_2.sizePolicy().hasHeightForWidth())
        self.cb_end_2.setSizePolicy(sizePolicy3)
        self.cb_end_2.setMinimumSize(QSize(64, 30))
        self.cb_end_2.setMaximumSize(QSize(70, 30))
        self.cb_end_2.setEditable(True)

        self.gridLayout.addWidget(self.cb_end_2, 2, 5, 1, 1)

        self.pb_preset_1 = QPushButton(self.page_divider)
        self.pb_preset_1.setObjectName(u"pb_preset_1")
        sizePolicy4.setHeightForWidth(self.pb_preset_1.sizePolicy().hasHeightForWidth())
        self.pb_preset_1.setSizePolicy(sizePolicy4)
        self.pb_preset_1.setMinimumSize(QSize(25, 30))
        self.pb_preset_1.setMaximumSize(QSize(25, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(True)
        self.pb_preset_1.setFont(font4)
        self.pb_preset_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_preset_1.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/plus.png);\n"
"	background-position: center center;\n"
"}")

        self.gridLayout.addWidget(self.pb_preset_1, 1, 6, 1, 1)

        self.cb_start_1 = QComboBox(self.page_divider)
        self.cb_start_1.addItem("")
        self.cb_start_1.setObjectName(u"cb_start_1")
        sizePolicy3.setHeightForWidth(self.cb_start_1.sizePolicy().hasHeightForWidth())
        self.cb_start_1.setSizePolicy(sizePolicy3)
        self.cb_start_1.setMinimumSize(QSize(64, 30))
        self.cb_start_1.setMaximumSize(QSize(70, 30))
        self.cb_start_1.setEditable(True)

        self.gridLayout.addWidget(self.cb_start_1, 1, 0, 1, 1)

        self.cb_start_5 = QComboBox(self.page_divider)
        self.cb_start_5.addItem("")
        self.cb_start_5.setObjectName(u"cb_start_5")
        sizePolicy5.setHeightForWidth(self.cb_start_5.sizePolicy().hasHeightForWidth())
        self.cb_start_5.setSizePolicy(sizePolicy5)
        self.cb_start_5.setMinimumSize(QSize(64, 30))
        self.cb_start_5.setMaximumSize(QSize(70, 30))
        self.cb_start_5.setEditable(True)

        self.gridLayout.addWidget(self.cb_start_5, 5, 0, 1, 1)

        self.le_check_2 = QLineEdit(self.page_divider)
        self.le_check_2.setObjectName(u"le_check_2")
        sizePolicy5.setHeightForWidth(self.le_check_2.sizePolicy().hasHeightForWidth())
        self.le_check_2.setSizePolicy(sizePolicy5)
        self.le_check_2.setMinimumSize(QSize(55, 30))
        self.le_check_2.setMaximumSize(QSize(50, 30))
        self.le_check_2.setReadOnly(True)

        self.gridLayout.addWidget(self.le_check_2, 2, 4, 1, 1)

        self.le_length_1 = QLineEdit(self.page_divider)
        self.le_length_1.setObjectName(u"le_length_1")
        sizePolicy5.setHeightForWidth(self.le_length_1.sizePolicy().hasHeightForWidth())
        self.le_length_1.setSizePolicy(sizePolicy5)
        self.le_length_1.setMinimumSize(QSize(55, 30))
        self.le_length_1.setMaximumSize(QSize(50, 30))
        self.le_length_1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_length_1, 1, 1, 1, 1)

        self.pb_send_1 = QPushButton(self.page_divider)
        self.pb_send_1.setObjectName(u"pb_send_1")
        sizePolicy4.setHeightForWidth(self.pb_send_1.sizePolicy().hasHeightForWidth())
        self.pb_send_1.setSizePolicy(sizePolicy4)
        self.pb_send_1.setMinimumSize(QSize(25, 30))
        self.pb_send_1.setMaximumSize(QSize(25, 30))
        self.pb_send_1.setFont(font)
        self.pb_send_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_1.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/arrow-right.png);\n"
"	background-position: center center;\n"
"	border-style: none;\n"
"}")

        self.gridLayout.addWidget(self.pb_send_1, 1, 7, 1, 1)

        self.cb_end_5 = QComboBox(self.page_divider)
        self.cb_end_5.addItem("")
        self.cb_end_5.setObjectName(u"cb_end_5")
        sizePolicy3.setHeightForWidth(self.cb_end_5.sizePolicy().hasHeightForWidth())
        self.cb_end_5.setSizePolicy(sizePolicy3)
        self.cb_end_5.setMinimumSize(QSize(64, 30))
        self.cb_end_5.setMaximumSize(QSize(70, 30))
        self.cb_end_5.setEditable(True)

        self.gridLayout.addWidget(self.cb_end_5, 5, 5, 1, 1)

        self.pb_preset_4 = QPushButton(self.page_divider)
        self.pb_preset_4.setObjectName(u"pb_preset_4")
        sizePolicy4.setHeightForWidth(self.pb_preset_4.sizePolicy().hasHeightForWidth())
        self.pb_preset_4.setSizePolicy(sizePolicy4)
        self.pb_preset_4.setMinimumSize(QSize(25, 30))
        self.pb_preset_4.setMaximumSize(QSize(25, 30))
        self.pb_preset_4.setFont(font)
        self.pb_preset_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_preset_4.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/plus.png);\n"
"	background-position: center center;\n"
"}")

        self.gridLayout.addWidget(self.pb_preset_4, 4, 6, 1, 1)

        self.cb_data_4 = QComboBox(self.page_divider)
        self.cb_data_4.addItem("")
        self.cb_data_4.setObjectName(u"cb_data_4")
        sizePolicy.setHeightForWidth(self.cb_data_4.sizePolicy().hasHeightForWidth())
        self.cb_data_4.setSizePolicy(sizePolicy)
        self.cb_data_4.setMinimumSize(QSize(55, 30))
        self.cb_data_4.setMaximumSize(QSize(16777215, 30))
        self.cb_data_4.setEditable(True)

        self.gridLayout.addWidget(self.cb_data_4, 4, 3, 1, 1)

        self.pb_send_2 = QPushButton(self.page_divider)
        self.pb_send_2.setObjectName(u"pb_send_2")
        sizePolicy4.setHeightForWidth(self.pb_send_2.sizePolicy().hasHeightForWidth())
        self.pb_send_2.setSizePolicy(sizePolicy4)
        self.pb_send_2.setMinimumSize(QSize(25, 30))
        self.pb_send_2.setMaximumSize(QSize(25, 30))
        self.pb_send_2.setFont(font)
        self.pb_send_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_2.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/arrow-right.png);\n"
"	background-position: center center;\n"
"	border-style: none;\n"
"}")

        self.gridLayout.addWidget(self.pb_send_2, 2, 7, 1, 1)

        self.pb_send_3 = QPushButton(self.page_divider)
        self.pb_send_3.setObjectName(u"pb_send_3")
        sizePolicy4.setHeightForWidth(self.pb_send_3.sizePolicy().hasHeightForWidth())
        self.pb_send_3.setSizePolicy(sizePolicy4)
        self.pb_send_3.setMinimumSize(QSize(25, 30))
        self.pb_send_3.setMaximumSize(QSize(25, 30))
        self.pb_send_3.setFont(font)
        self.pb_send_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_3.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/arrow-right.png);\n"
"	background-position: center center;\n"
"	border-style: none;\n"
"}")

        self.gridLayout.addWidget(self.pb_send_3, 3, 7, 1, 1)

        self.cb_data_3 = QComboBox(self.page_divider)
        self.cb_data_3.addItem("")
        self.cb_data_3.setObjectName(u"cb_data_3")
        sizePolicy.setHeightForWidth(self.cb_data_3.sizePolicy().hasHeightForWidth())
        self.cb_data_3.setSizePolicy(sizePolicy)
        self.cb_data_3.setMinimumSize(QSize(55, 30))
        self.cb_data_3.setMaximumSize(QSize(16777215, 30))
        self.cb_data_3.setEditable(True)

        self.gridLayout.addWidget(self.cb_data_3, 3, 3, 1, 1)

        self.lbl_stop = QLabel(self.page_divider)
        self.lbl_stop.setObjectName(u"lbl_stop")
        sizePolicy3.setHeightForWidth(self.lbl_stop.sizePolicy().hasHeightForWidth())
        self.lbl_stop.setSizePolicy(sizePolicy3)
        self.lbl_stop.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout.addWidget(self.lbl_stop, 0, 5, 1, 1)

        self.cb_end_4 = QComboBox(self.page_divider)
        self.cb_end_4.addItem("")
        self.cb_end_4.setObjectName(u"cb_end_4")
        sizePolicy3.setHeightForWidth(self.cb_end_4.sizePolicy().hasHeightForWidth())
        self.cb_end_4.setSizePolicy(sizePolicy3)
        self.cb_end_4.setMinimumSize(QSize(64, 30))
        self.cb_end_4.setMaximumSize(QSize(70, 30))
        self.cb_end_4.setEditable(True)

        self.gridLayout.addWidget(self.cb_end_4, 4, 5, 1, 1)

        self.cb_data_1 = QComboBox(self.page_divider)
        self.cb_data_1.addItem("")
        self.cb_data_1.setObjectName(u"cb_data_1")
        sizePolicy.setHeightForWidth(self.cb_data_1.sizePolicy().hasHeightForWidth())
        self.cb_data_1.setSizePolicy(sizePolicy)
        self.cb_data_1.setMinimumSize(QSize(55, 30))
        self.cb_data_1.setMaximumSize(QSize(16777215, 30))
        self.cb_data_1.setEditable(True)

        self.gridLayout.addWidget(self.cb_data_1, 1, 3, 1, 1)

        self.le_check_3 = QLineEdit(self.page_divider)
        self.le_check_3.setObjectName(u"le_check_3")
        sizePolicy5.setHeightForWidth(self.le_check_3.sizePolicy().hasHeightForWidth())
        self.le_check_3.setSizePolicy(sizePolicy5)
        self.le_check_3.setMinimumSize(QSize(55, 30))
        self.le_check_3.setMaximumSize(QSize(50, 30))
        self.le_check_3.setReadOnly(True)

        self.gridLayout.addWidget(self.le_check_3, 3, 4, 1, 1)

        self.cb_start_4 = QComboBox(self.page_divider)
        self.cb_start_4.addItem("")
        self.cb_start_4.setObjectName(u"cb_start_4")
        sizePolicy5.setHeightForWidth(self.cb_start_4.sizePolicy().hasHeightForWidth())
        self.cb_start_4.setSizePolicy(sizePolicy5)
        self.cb_start_4.setMinimumSize(QSize(64, 30))
        self.cb_start_4.setMaximumSize(QSize(70, 30))
        self.cb_start_4.setEditable(True)

        self.gridLayout.addWidget(self.cb_start_4, 4, 0, 1, 1)

        self.le_length_4 = QLineEdit(self.page_divider)
        self.le_length_4.setObjectName(u"le_length_4")
        sizePolicy5.setHeightForWidth(self.le_length_4.sizePolicy().hasHeightForWidth())
        self.le_length_4.setSizePolicy(sizePolicy5)
        self.le_length_4.setMinimumSize(QSize(55, 30))
        self.le_length_4.setMaximumSize(QSize(50, 30))
        self.le_length_4.setReadOnly(True)

        self.gridLayout.addWidget(self.le_length_4, 4, 1, 1, 1)

        self.le_length_5 = QLineEdit(self.page_divider)
        self.le_length_5.setObjectName(u"le_length_5")
        sizePolicy5.setHeightForWidth(self.le_length_5.sizePolicy().hasHeightForWidth())
        self.le_length_5.setSizePolicy(sizePolicy5)
        self.le_length_5.setMinimumSize(QSize(55, 30))
        self.le_length_5.setMaximumSize(QSize(50, 30))
        self.le_length_5.setReadOnly(True)

        self.gridLayout.addWidget(self.le_length_5, 5, 1, 1, 1)

        self.pb_preset_5 = QPushButton(self.page_divider)
        self.pb_preset_5.setObjectName(u"pb_preset_5")
        sizePolicy4.setHeightForWidth(self.pb_preset_5.sizePolicy().hasHeightForWidth())
        self.pb_preset_5.setSizePolicy(sizePolicy4)
        self.pb_preset_5.setMinimumSize(QSize(25, 30))
        self.pb_preset_5.setMaximumSize(QSize(25, 30))
        self.pb_preset_5.setFont(font)
        self.pb_preset_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_preset_5.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/plus.png);\n"
"	background-position: center center;\n"
"}")

        self.gridLayout.addWidget(self.pb_preset_5, 5, 6, 1, 1)

        self.le_check_1 = QLineEdit(self.page_divider)
        self.le_check_1.setObjectName(u"le_check_1")
        sizePolicy5.setHeightForWidth(self.le_check_1.sizePolicy().hasHeightForWidth())
        self.le_check_1.setSizePolicy(sizePolicy5)
        self.le_check_1.setMinimumSize(QSize(55, 30))
        self.le_check_1.setMaximumSize(QSize(50, 30))
        self.le_check_1.setReadOnly(True)

        self.gridLayout.addWidget(self.le_check_1, 1, 4, 1, 1)

        self.cb_command_1 = QComboBox(self.page_divider)
        self.cb_command_1.addItem("")
        self.cb_command_1.addItem("")
        self.cb_command_1.addItem("")
        self.cb_command_1.setObjectName(u"cb_command_1")
        sizePolicy3.setHeightForWidth(self.cb_command_1.sizePolicy().hasHeightForWidth())
        self.cb_command_1.setSizePolicy(sizePolicy3)
        self.cb_command_1.setMinimumSize(QSize(64, 30))
        self.cb_command_1.setMaximumSize(QSize(70, 30))
        self.cb_command_1.setEditable(True)

        self.gridLayout.addWidget(self.cb_command_1, 1, 2, 1, 1)

        self.lbl_command = QLabel(self.page_divider)
        self.lbl_command.setObjectName(u"lbl_command")
        sizePolicy3.setHeightForWidth(self.lbl_command.sizePolicy().hasHeightForWidth())
        self.lbl_command.setSizePolicy(sizePolicy3)
        self.lbl_command.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout.addWidget(self.lbl_command, 0, 2, 1, 1)

        self.lbl_length = QLabel(self.page_divider)
        self.lbl_length.setObjectName(u"lbl_length")
        sizePolicy3.setHeightForWidth(self.lbl_length.sizePolicy().hasHeightForWidth())
        self.lbl_length.setSizePolicy(sizePolicy3)
        self.lbl_length.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.gridLayout.addWidget(self.lbl_length, 0, 1, 1, 1)

        self.cb_command_2 = QComboBox(self.page_divider)
        self.cb_command_2.addItem("")
        self.cb_command_2.addItem("")
        self.cb_command_2.addItem("")
        self.cb_command_2.setObjectName(u"cb_command_2")
        sizePolicy3.setHeightForWidth(self.cb_command_2.sizePolicy().hasHeightForWidth())
        self.cb_command_2.setSizePolicy(sizePolicy3)
        self.cb_command_2.setMinimumSize(QSize(64, 30))
        self.cb_command_2.setMaximumSize(QSize(70, 30))
        self.cb_command_2.setEditable(True)

        self.gridLayout.addWidget(self.cb_command_2, 2, 2, 1, 1)

        self.cb_command_3 = QComboBox(self.page_divider)
        self.cb_command_3.addItem("")
        self.cb_command_3.addItem("")
        self.cb_command_3.addItem("")
        self.cb_command_3.setObjectName(u"cb_command_3")
        sizePolicy3.setHeightForWidth(self.cb_command_3.sizePolicy().hasHeightForWidth())
        self.cb_command_3.setSizePolicy(sizePolicy3)
        self.cb_command_3.setMinimumSize(QSize(64, 30))
        self.cb_command_3.setMaximumSize(QSize(70, 30))
        self.cb_command_3.setEditable(True)

        self.gridLayout.addWidget(self.cb_command_3, 3, 2, 1, 1)

        self.cb_command_4 = QComboBox(self.page_divider)
        self.cb_command_4.addItem("")
        self.cb_command_4.addItem("")
        self.cb_command_4.addItem("")
        self.cb_command_4.setObjectName(u"cb_command_4")
        sizePolicy3.setHeightForWidth(self.cb_command_4.sizePolicy().hasHeightForWidth())
        self.cb_command_4.setSizePolicy(sizePolicy3)
        self.cb_command_4.setMinimumSize(QSize(64, 30))
        self.cb_command_4.setMaximumSize(QSize(70, 30))
        self.cb_command_4.setAutoFillBackground(False)
        self.cb_command_4.setEditable(True)

        self.gridLayout.addWidget(self.cb_command_4, 4, 2, 1, 1)

        self.cb_command_5 = QComboBox(self.page_divider)
        self.cb_command_5.addItem("")
        self.cb_command_5.addItem("")
        self.cb_command_5.addItem("")
        self.cb_command_5.setObjectName(u"cb_command_5")
        sizePolicy3.setHeightForWidth(self.cb_command_5.sizePolicy().hasHeightForWidth())
        self.cb_command_5.setSizePolicy(sizePolicy3)
        self.cb_command_5.setMinimumSize(QSize(64, 30))
        self.cb_command_5.setMaximumSize(QSize(70, 30))
        self.cb_command_5.setEditable(True)

        self.gridLayout.addWidget(self.cb_command_5, 5, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 1)
        self.gridLayout.setColumnStretch(7, 1)

        self.verticalLayout_12.addLayout(self.gridLayout)

        self.labelBoxBlenderInstalation_5 = QLabel(self.page_divider)
        self.labelBoxBlenderInstalation_5.setObjectName(u"labelBoxBlenderInstalation_5")
        sizePolicy4.setHeightForWidth(self.labelBoxBlenderInstalation_5.sizePolicy().hasHeightForWidth())
        self.labelBoxBlenderInstalation_5.setSizePolicy(sizePolicy4)
        self.labelBoxBlenderInstalation_5.setFont(font)
        self.labelBoxBlenderInstalation_5.setStyleSheet(u"QLabel {\n"
"	margin-top: 10px;\n"
"}")

        self.verticalLayout_12.addWidget(self.labelBoxBlenderInstalation_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.horizontalLayout_6.addLayout(self.verticalLayout_19)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_preset_previous = QPushButton(self.page_divider)
        self.btn_preset_previous.setObjectName(u"btn_preset_previous")
        sizePolicy4.setHeightForWidth(self.btn_preset_previous.sizePolicy().hasHeightForWidth())
        self.btn_preset_previous.setSizePolicy(sizePolicy4)
        self.btn_preset_previous.setMinimumSize(QSize(0, 30))
        self.btn_preset_previous.setMaximumSize(QSize(30, 30))
        self.btn_preset_previous.setStyleSheet(u"background-image: url(:/icons/images/icons/chevron-left.png);\n"
"background-position: center center;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;")

        self.horizontalLayout_15.addWidget(self.btn_preset_previous)

        self.le_preset_num = QLineEdit(self.page_divider)
        self.le_preset_num.setObjectName(u"le_preset_num")
        sizePolicy4.setHeightForWidth(self.le_preset_num.sizePolicy().hasHeightForWidth())
        self.le_preset_num.setSizePolicy(sizePolicy4)
        self.le_preset_num.setMinimumSize(QSize(30, 30))
        self.le_preset_num.setMaximumSize(QSize(30, 30))
        self.le_preset_num.setStyleSheet(u"border-radius: 0px;")
        self.le_preset_num.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.le_preset_num)

        self.btn_preset_next = QPushButton(self.page_divider)
        self.btn_preset_next.setObjectName(u"btn_preset_next")
        sizePolicy4.setHeightForWidth(self.btn_preset_next.sizePolicy().hasHeightForWidth())
        self.btn_preset_next.setSizePolicy(sizePolicy4)
        self.btn_preset_next.setMinimumSize(QSize(30, 30))
        self.btn_preset_next.setMaximumSize(QSize(30, 30))
        self.btn_preset_next.setStyleSheet(u"background-image: url(:/icons/images/icons/chevron-right.png);\n"
"background-position: center center;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;")

        self.horizontalLayout_15.addWidget(self.btn_preset_next)

        self.le_preset_name = QLineEdit(self.page_divider)
        self.le_preset_name.setObjectName(u"le_preset_name")
        sizePolicy.setHeightForWidth(self.le_preset_name.sizePolicy().hasHeightForWidth())
        self.le_preset_name.setSizePolicy(sizePolicy)
        self.le_preset_name.setMinimumSize(QSize(50, 30))
        self.le_preset_name.setMaximumSize(QSize(16777215, 30))
        self.le_preset_name.setStyleSheet(u"margin: 0px 0px 0px 15px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;")

        self.horizontalLayout_15.addWidget(self.le_preset_name)

        self.btn_preset_add = QPushButton(self.page_divider)
        self.btn_preset_add.setObjectName(u"btn_preset_add")
        sizePolicy4.setHeightForWidth(self.btn_preset_add.sizePolicy().hasHeightForWidth())
        self.btn_preset_add.setSizePolicy(sizePolicy4)
        self.btn_preset_add.setMinimumSize(QSize(0, 30))
        self.btn_preset_add.setMaximumSize(QSize(30, 30))
        self.btn_preset_add.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/plus.png);\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background-position: center center;\n"
"	background-color: rgb(54,106,206);\n"
"	border-style: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(48,95,185);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45,89,173);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(52, 59, 72);\n"
"}")

        self.horizontalLayout_15.addWidget(self.btn_preset_add)


        self.verticalLayout_22.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(25)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.sb_camera_a = QSpinBox(self.page_divider)
        self.sb_camera_a.setObjectName(u"sb_camera_a")
        sizePolicy.setHeightForWidth(self.sb_camera_a.sizePolicy().hasHeightForWidth())
        self.sb_camera_a.setSizePolicy(sizePolicy)
        self.sb_camera_a.setMinimumSize(QSize(0, 30))
        self.sb_camera_a.setMaximumSize(QSize(16777215, 30))
        self.sb_camera_a.setStyleSheet(u"QSpinBox {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-position: center right;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.sb_camera_a.setMaximum(2147483647)
        self.sb_camera_a.setSingleStep(100)
        self.sb_camera_a.setValue(100)

        self.gridLayout_2.addWidget(self.sb_camera_a, 0, 0, 1, 1)

        self.pb_send_camera_a = QPushButton(self.page_divider)
        self.pb_send_camera_a.setObjectName(u"pb_send_camera_a")
        sizePolicy4.setHeightForWidth(self.pb_send_camera_a.sizePolicy().hasHeightForWidth())
        self.pb_send_camera_a.setSizePolicy(sizePolicy4)
        self.pb_send_camera_a.setMinimumSize(QSize(30, 30))
        self.pb_send_camera_a.setMaximumSize(QSize(30, 30))
        self.pb_send_camera_a.setFont(font)
        self.pb_send_camera_a.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_camera_a.setStyleSheet(u"QPushButton {\n"
"/*\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-origin: margin;\n"
"	background-position: center left;\n"
"	padding-left: 24px;\n"
"*/\n"
"	margin-left: -3px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.pb_send_camera_a, 0, 1, 1, 1)

        self.pb_send_camera_b = QPushButton(self.page_divider)
        self.pb_send_camera_b.setObjectName(u"pb_send_camera_b")
        sizePolicy4.setHeightForWidth(self.pb_send_camera_b.sizePolicy().hasHeightForWidth())
        self.pb_send_camera_b.setSizePolicy(sizePolicy4)
        self.pb_send_camera_b.setMinimumSize(QSize(30, 30))
        self.pb_send_camera_b.setMaximumSize(QSize(30, 30))
        self.pb_send_camera_b.setFont(font)
        self.pb_send_camera_b.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_camera_b.setStyleSheet(u"QPushButton {\n"
"/*\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-origin: margin;\n"
"	background-position: center left;\n"
"	padding-left: 24px;\n"
"*/\n"
"	margin-left: -3px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.pb_send_camera_b, 1, 1, 1, 1)

        self.sb_camera_c = QSpinBox(self.page_divider)
        self.sb_camera_c.setObjectName(u"sb_camera_c")
        sizePolicy.setHeightForWidth(self.sb_camera_c.sizePolicy().hasHeightForWidth())
        self.sb_camera_c.setSizePolicy(sizePolicy)
        self.sb_camera_c.setMinimumSize(QSize(0, 30))
        self.sb_camera_c.setMaximumSize(QSize(16777215, 30))
        self.sb_camera_c.setStyleSheet(u"QSpinBox {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-position: center right;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.sb_camera_c.setMaximum(2147483647)
        self.sb_camera_c.setSingleStep(100)
        self.sb_camera_c.setValue(100)

        self.gridLayout_2.addWidget(self.sb_camera_c, 2, 0, 1, 1)

        self.pb_send_camera_c = QPushButton(self.page_divider)
        self.pb_send_camera_c.setObjectName(u"pb_send_camera_c")
        sizePolicy4.setHeightForWidth(self.pb_send_camera_c.sizePolicy().hasHeightForWidth())
        self.pb_send_camera_c.setSizePolicy(sizePolicy4)
        self.pb_send_camera_c.setMinimumSize(QSize(30, 30))
        self.pb_send_camera_c.setMaximumSize(QSize(30, 30))
        self.pb_send_camera_c.setFont(font)
        self.pb_send_camera_c.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_camera_c.setStyleSheet(u"QPushButton {\n"
"/*\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-origin: margin;\n"
"	background-position: center left;\n"
"	padding-left: 24px;\n"
"*/\n"
"	margin-left: -3px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.pb_send_camera_c, 2, 1, 1, 1)

        self.sb_camera_d = QSpinBox(self.page_divider)
        self.sb_camera_d.setObjectName(u"sb_camera_d")
        sizePolicy.setHeightForWidth(self.sb_camera_d.sizePolicy().hasHeightForWidth())
        self.sb_camera_d.setSizePolicy(sizePolicy)
        self.sb_camera_d.setMinimumSize(QSize(0, 30))
        self.sb_camera_d.setMaximumSize(QSize(16777215, 30))
        self.sb_camera_d.setStyleSheet(u"QSpinBox {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-position: center right;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.sb_camera_d.setMaximum(2147483647)
        self.sb_camera_d.setSingleStep(100)
        self.sb_camera_d.setValue(100)

        self.gridLayout_2.addWidget(self.sb_camera_d, 3, 0, 1, 1)

        self.pb_send_camera_d = QPushButton(self.page_divider)
        self.pb_send_camera_d.setObjectName(u"pb_send_camera_d")
        sizePolicy4.setHeightForWidth(self.pb_send_camera_d.sizePolicy().hasHeightForWidth())
        self.pb_send_camera_d.setSizePolicy(sizePolicy4)
        self.pb_send_camera_d.setMinimumSize(QSize(30, 30))
        self.pb_send_camera_d.setMaximumSize(QSize(30, 30))
        self.pb_send_camera_d.setFont(font)
        self.pb_send_camera_d.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_camera_d.setStyleSheet(u"QPushButton {\n"
"/*\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-origin: margin;\n"
"	background-position: center left;\n"
"	padding-left: 24px;\n"
"*/\n"
"	margin-left: -3px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.pb_send_camera_d, 3, 1, 1, 1)

        self.sb_camera_b = QSpinBox(self.page_divider)
        self.sb_camera_b.setObjectName(u"sb_camera_b")
        sizePolicy.setHeightForWidth(self.sb_camera_b.sizePolicy().hasHeightForWidth())
        self.sb_camera_b.setSizePolicy(sizePolicy)
        self.sb_camera_b.setMinimumSize(QSize(0, 30))
        self.sb_camera_b.setMaximumSize(QSize(16777215, 30))
        self.sb_camera_b.setStyleSheet(u"QSpinBox {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-position: center right;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.sb_camera_b.setMaximum(2147483647)
        self.sb_camera_b.setSingleStep(100)
        self.sb_camera_b.setValue(100)

        self.gridLayout_2.addWidget(self.sb_camera_b, 1, 0, 1, 1)


        self.horizontalLayout_16.addLayout(self.gridLayout_2)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, -1, -1)
        self.sb_valve = QSpinBox(self.page_divider)
        self.sb_valve.setObjectName(u"sb_valve")
        sizePolicy.setHeightForWidth(self.sb_valve.sizePolicy().hasHeightForWidth())
        self.sb_valve.setSizePolicy(sizePolicy)
        self.sb_valve.setMinimumSize(QSize(0, 30))
        self.sb_valve.setMaximumSize(QSize(16777215, 30))
        self.sb_valve.setStyleSheet(u"QSpinBox {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background-image: url(:/icons/images/icons/wind.png);\n"
"	background-position: center right;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.sb_valve.setMaximum(2147483647)
        self.sb_valve.setSingleStep(100)
        self.sb_valve.setValue(100)

        self.horizontalLayout_18.addWidget(self.sb_valve)

        self.pb_send_valve = QPushButton(self.page_divider)
        self.pb_send_valve.setObjectName(u"pb_send_valve")
        sizePolicy4.setHeightForWidth(self.pb_send_valve.sizePolicy().hasHeightForWidth())
        self.pb_send_valve.setSizePolicy(sizePolicy4)
        self.pb_send_valve.setMinimumSize(QSize(30, 30))
        self.pb_send_valve.setMaximumSize(QSize(30, 30))
        self.pb_send_valve.setFont(font)
        self.pb_send_valve.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_valve.setStyleSheet(u"QPushButton {\n"
"/*\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-origin: margin;\n"
"	background-position: center left;\n"
"	padding-left: 24px;\n"
"*/\n"
"	margin-left: -3px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"\n"
"}")

        self.horizontalLayout_18.addWidget(self.pb_send_valve)


        self.verticalLayout_21.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, -1, -1, -1)
        self.cb_from_camera = QComboBox(self.page_divider)
        self.cb_from_camera.addItem("")
        self.cb_from_camera.addItem("")
        self.cb_from_camera.addItem("")
        self.cb_from_camera.addItem("")
        self.cb_from_camera.setObjectName(u"cb_from_camera")
        sizePolicy4.setHeightForWidth(self.cb_from_camera.sizePolicy().hasHeightForWidth())
        self.cb_from_camera.setSizePolicy(sizePolicy4)
        self.cb_from_camera.setMinimumSize(QSize(75, 30))
        self.cb_from_camera.setMaximumSize(QSize(16777215, 30))
        self.cb_from_camera.setStyleSheet(u"QComboBox {\n"
"	border-radius: 5px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	margin-right: -1px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-position: top left;\n"
"	border: none;\n"
"	border-right: 3px solid rgba(39, 44, 54, 150);\n"
"	border-radius: 0px;\n"
"	border-top-left-radius: 3px;\n"
"	border-bottom-left-radius: 3px;	\n"
" }")
        self.cb_from_camera.setEditable(True)

        self.horizontalLayout_17.addWidget(self.cb_from_camera)

        self.le_to_valve = QLineEdit(self.page_divider)
        self.le_to_valve.setObjectName(u"le_to_valve")
        sizePolicy.setHeightForWidth(self.le_to_valve.sizePolicy().hasHeightForWidth())
        self.le_to_valve.setSizePolicy(sizePolicy)
        self.le_to_valve.setMinimumSize(QSize(40, 30))
        self.le_to_valve.setMaximumSize(QSize(80, 30))
        self.le_to_valve.setStyleSheet(u"border-radius: 0px;\n"
"background-image: url(:/icons/images/icons/link-2.png);\n"
"background-position: center right;\n"
"background-repeat: no-repeat;")

        self.horizontalLayout_17.addWidget(self.le_to_valve)

        self.pb_send_to_valve = QPushButton(self.page_divider)
        self.pb_send_to_valve.setObjectName(u"pb_send_to_valve")
        sizePolicy4.setHeightForWidth(self.pb_send_to_valve.sizePolicy().hasHeightForWidth())
        self.pb_send_to_valve.setSizePolicy(sizePolicy4)
        self.pb_send_to_valve.setMinimumSize(QSize(30, 30))
        self.pb_send_to_valve.setMaximumSize(QSize(30, 30))
        self.pb_send_to_valve.setFont(font)
        self.pb_send_to_valve.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_to_valve.setStyleSheet(u"QPushButton {\n"
"/*\n"
"	background-image: url(:/icons/images/icons/camera.png);\n"
"	background-origin: margin;\n"
"	background-position: center left;\n"
"	padding-left: 24px;\n"
"*/\n"
"	margin-left: -3px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"\n"
"}")

        self.horizontalLayout_17.addWidget(self.pb_send_to_valve)


        self.verticalLayout_21.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, -1, -1, -1)
        self.horizontalSlider = QSlider(self.page_divider)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QSize(0, 30))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.horizontalSlider)

        self.horizontalSlider_2 = QSlider(self.page_divider)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        sizePolicy.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setMinimumSize(QSize(0, 30))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.horizontalSlider_2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_2)

        self.pb_divider_restore = QPushButton(self.page_divider)
        self.pb_divider_restore.setObjectName(u"pb_divider_restore")
        sizePolicy4.setHeightForWidth(self.pb_divider_restore.sizePolicy().hasHeightForWidth())
        self.pb_divider_restore.setSizePolicy(sizePolicy4)
        self.pb_divider_restore.setMinimumSize(QSize(30, 30))
        self.pb_divider_restore.setMaximumSize(QSize(30, 30))
        self.pb_divider_restore.setFont(font4)
        self.pb_divider_restore.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_divider_restore.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/rotate-ccw.png);\n"
"	background-position: center center;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.pb_divider_restore)

        self.pb_divider_random = QPushButton(self.page_divider)
        self.pb_divider_random.setObjectName(u"pb_divider_random")
        sizePolicy4.setHeightForWidth(self.pb_divider_random.sizePolicy().hasHeightForWidth())
        self.pb_divider_random.setSizePolicy(sizePolicy4)
        self.pb_divider_random.setMinimumSize(QSize(30, 30))
        self.pb_divider_random.setMaximumSize(QSize(30, 30))
        self.pb_divider_random.setFont(font4)
        self.pb_divider_random.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_divider_random.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/shuffle.png);\n"
"	background-position: center center;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_20.addWidget(self.pb_divider_random)

        self.pb_send_camera_all = QPushButton(self.page_divider)
        self.pb_send_camera_all.setObjectName(u"pb_send_camera_all")
        sizePolicy4.setHeightForWidth(self.pb_send_camera_all.sizePolicy().hasHeightForWidth())
        self.pb_send_camera_all.setSizePolicy(sizePolicy4)
        self.pb_send_camera_all.setMinimumSize(QSize(30, 30))
        self.pb_send_camera_all.setMaximumSize(QSize(30, 30))
        self.pb_send_camera_all.setFont(font4)
        self.pb_send_camera_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_camera_all.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/images/icons/arrow-right.png);\n"
"	background-position: center center;\n"
"	background-color: rgb(54,106,206);\n"
"	border-style: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(48,95,185);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(45,89,173);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"")

        self.horizontalLayout_20.addWidget(self.pb_send_camera_all)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_16.addLayout(self.verticalLayout_21)


        self.verticalLayout_22.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_22)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 6)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_11.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.labelBoxBlenderInstalation_6 = QLabel(self.page_divider)
        self.labelBoxBlenderInstalation_6.setObjectName(u"labelBoxBlenderInstalation_6")
        sizePolicy4.setHeightForWidth(self.labelBoxBlenderInstalation_6.sizePolicy().hasHeightForWidth())
        self.labelBoxBlenderInstalation_6.setSizePolicy(sizePolicy4)
        self.labelBoxBlenderInstalation_6.setFont(font)
        self.labelBoxBlenderInstalation_6.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.labelBoxBlenderInstalation_6)

        self.lv_packets = QListView(self.page_divider)
        self.lv_packets.setObjectName(u"lv_packets")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lv_packets.sizePolicy().hasHeightForWidth())
        self.lv_packets.setSizePolicy(sizePolicy6)
        self.lv_packets.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_11.addWidget(self.lv_packets)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pb_send_start = QPushButton(self.page_divider)
        self.pb_send_start.setObjectName(u"pb_send_start")
        sizePolicy4.setHeightForWidth(self.pb_send_start.sizePolicy().hasHeightForWidth())
        self.pb_send_start.setSizePolicy(sizePolicy4)
        self.pb_send_start.setMinimumSize(QSize(90, 30))
        self.pb_send_start.setMaximumSize(QSize(90, 30))
        self.pb_send_start.setFont(font4)
        self.pb_send_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_start.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(87,150,92);\n"
"	background-origin: border;\n"
"	background-image: url(:/icons/images/icons/camera-and-down.png);\n"
"	padding-left: 6px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border: none;\n"
"	margin-right: -1px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(78,135,82);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(73,126,77);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(52, 59, 72);\n"
"}")

        self.horizontalLayout_14.addWidget(self.pb_send_start)

        self.widget = QWidget(self.page_divider)
        self.widget.setObjectName(u"widget")
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.widget.setMinimumSize(QSize(1, 30))
        self.widget.setMaximumSize(QSize(1, 30))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(87,150,92);\n"
"	background-image: url(:/icons/images/icons/30-height-sep.png);\n"
"	border: none;\n"
"	border-top: 5px solid rgb(87,150,92);\n"
"	border-bottom: 5px solid rgb(87,150,92);\n"
"	margin-right: -1px;\n"
"}\n"
"QWidget:disabled {\n"
"	background-color: rgb(52, 59, 72);\n"
"	border-top: 5px solid rgb(52, 59, 72);\n"
"	border-bottom: 5px solid rgb(52, 59, 72);\n"
"}")

        self.horizontalLayout_14.addWidget(self.widget)

        self.pb_send_start_2 = QPushButton(self.page_divider)
        self.pb_send_start_2.setObjectName(u"pb_send_start_2")
        sizePolicy4.setHeightForWidth(self.pb_send_start_2.sizePolicy().hasHeightForWidth())
        self.pb_send_start_2.setSizePolicy(sizePolicy4)
        self.pb_send_start_2.setMinimumSize(QSize(30, 30))
        self.pb_send_start_2.setMaximumSize(QSize(30, 30))
        self.pb_send_start_2.setFont(font4)
        self.pb_send_start_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_start_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(87,150,92);\n"
"	background-origin: border;\n"
"	border-style: none;\n"
"	background-image: url(:/icons/images/icons/play.png);\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(78,135,82);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(73,126,77);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(52, 59, 72);\n"
"}")

        self.horizontalLayout_14.addWidget(self.pb_send_start_2)

        self.widget_2 = QWidget(self.page_divider)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(10, 0))

        self.horizontalLayout_14.addWidget(self.widget_2)

        self.pb_send_stop = QPushButton(self.page_divider)
        self.pb_send_stop.setObjectName(u"pb_send_stop")
        sizePolicy4.setHeightForWidth(self.pb_send_stop.sizePolicy().hasHeightForWidth())
        self.pb_send_stop.setSizePolicy(sizePolicy4)
        self.pb_send_stop.setMinimumSize(QSize(30, 30))
        self.pb_send_stop.setMaximumSize(QSize(30, 30))
        self.pb_send_stop.setFont(font4)
        self.pb_send_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_send_stop.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(235,113,113);\n"
"	border-style: none;\n"
"	background-image: url(:/icons/images/icons/square.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(227,82,82);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(201,79,79);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(52, 59, 72);\n"
"}")

        self.horizontalLayout_14.addWidget(self.pb_send_stop)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_11.addLayout(self.verticalLayout_11)

        self.horizontalLayout_11.setStretch(0, 3)
        self.horizontalLayout_11.setStretch(1, 2)
        self.stackedWidget.addWidget(self.page_divider)
        self.page_valvedata = QWidget()
        self.page_valvedata.setObjectName(u"page_valvedata")
        self.verticalLayout_10 = QVBoxLayout(self.page_valvedata)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 5, 10, 10)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelBoxBlenderInstalation_2 = QLabel(self.page_valvedata)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.labelBoxBlenderInstalation_2)

        self.pb_export_table = QPushButton(self.page_valvedata)
        self.pb_export_table.setObjectName(u"pb_export_table")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pb_export_table.sizePolicy().hasHeightForWidth())
        self.pb_export_table.setSizePolicy(sizePolicy7)
        self.pb_export_table.setMinimumSize(QSize(75, 30))
        self.pb_export_table.setMaximumSize(QSize(100, 16777215))
        self.pb_export_table.setFont(font)
        self.pb_export_table.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_export_table.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_export_table.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.pb_export_table)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.tableView = QTableView(self.page_valvedata)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_10.addWidget(self.tableView)

        self.stackedWidget.addWidget(self.page_valvedata)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbl_server_addr = QLabel(self.bottomBar)
        self.lbl_server_addr.setObjectName(u"lbl_server_addr")
        sizePolicy7.setHeightForWidth(self.lbl_server_addr.sizePolicy().hasHeightForWidth())
        self.lbl_server_addr.setSizePolicy(sizePolicy7)
        self.lbl_server_addr.setMinimumSize(QSize(0, 0))
        self.lbl_server_addr.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.lbl_server_addr.setFont(font5)
        self.lbl_server_addr.setStyleSheet(u"QLabel {\n"
"	text-align: right;\n"
"	padding-right:0px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.lbl_server_addr)

        self.label_2 = QLabel(self.bottomBar)
        self.label_2.setObjectName(u"label_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy8)
        self.label_2.setMaximumSize(QSize(25, 16777215))
        self.label_2.setStyleSheet(u"background-image: url(:/icons/images/icons/link.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lbl_client_addr = QLabel(self.bottomBar)
        self.lbl_client_addr.setObjectName(u"lbl_client_addr")
        self.lbl_client_addr.setStyleSheet(u"QLabel {\n"
"	padding-left:0px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.lbl_client_addr)

        self.lbl_datagram = QLabel(self.bottomBar)
        self.lbl_datagram.setObjectName(u"lbl_datagram")
        sizePolicy1.setHeightForWidth(self.lbl_datagram.sizePolicy().hasHeightForWidth())
        self.lbl_datagram.setSizePolicy(sizePolicy1)
        self.lbl_datagram.setMaximumSize(QSize(16777215, 16))
        self.lbl_datagram.setFont(font5)
        self.lbl_datagram.setStyleSheet(u"")
        self.lbl_datagram.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lbl_datagram)

        self.label_1 = QLabel(self.bottomBar)
        self.label_1.setObjectName(u"label_1")
        sizePolicy8.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy8)
        self.label_1.setMinimumSize(QSize(12, 0))
        self.label_1.setMaximumSize(QSize(12, 16777215))
        self.label_1.setStyleSheet(u"QLabel {\n"
"	background-image: url(:/icons/images/icons/chevron-statusbarup.png);\n"
"	background-repeat:no-repeat;\n"
"	background-position: center center;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_1)

        self.lbl_tx_count = QLabel(self.bottomBar)
        self.lbl_tx_count.setObjectName(u"lbl_tx_count")
        self.lbl_tx_count.setStyleSheet(u"QLabel {\n"
"padding-left:0px;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.lbl_tx_count)

        self.label_3 = QLabel(self.bottomBar)
        self.label_3.setObjectName(u"label_3")
        sizePolicy8.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy8)
        self.label_3.setMinimumSize(QSize(12, 0))
        self.label_3.setMaximumSize(QSize(12, 16777215))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	background-image: url(:/icons/images/icons/chevron-statusbardown.png);\n"
"	background-repeat:no-repeat;\n"
"	background-position: center center;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lbl_rx_count = QLabel(self.bottomBar)
        self.lbl_rx_count.setObjectName(u"lbl_rx_count")
        self.lbl_rx_count.setStyleSheet(u"QLabel {\n"
"padding-left:0px;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.lbl_rx_count)

        self.lbl_version = QLabel(self.bottomBar)
        self.lbl_version.setObjectName(u"lbl_version")
        sizePolicy7.setHeightForWidth(self.lbl_version.sizePolicy().hasHeightForWidth())
        self.lbl_version.setSizePolicy(sizePolicy7)
        self.lbl_version.setMaximumSize(QSize(16777215, 16))
        self.lbl_version.setFont(font5)
        self.lbl_version.setTextFormat(Qt.PlainText)
        self.lbl_version.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lbl_version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-size-grip.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right bottom")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
        QWidget.setTabOrder(self.toggleButton, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_connection)
        QWidget.setTabOrder(self.btn_connection, self.btn_divider)
        QWidget.setTabOrder(self.btn_divider, self.btn_valvedata)
        QWidget.setTabOrder(self.btn_valvedata, self.cb_start_1)
        QWidget.setTabOrder(self.cb_start_1, self.le_length_1)
        QWidget.setTabOrder(self.le_length_1, self.cb_command_1)
        QWidget.setTabOrder(self.cb_command_1, self.cb_data_1)
        QWidget.setTabOrder(self.cb_data_1, self.le_check_1)
        QWidget.setTabOrder(self.le_check_1, self.cb_end_1)
        QWidget.setTabOrder(self.cb_end_1, self.pb_preset_1)
        QWidget.setTabOrder(self.pb_preset_1, self.pb_send_1)
        QWidget.setTabOrder(self.pb_send_1, self.cb_start_2)
        QWidget.setTabOrder(self.cb_start_2, self.le_length_2)
        QWidget.setTabOrder(self.le_length_2, self.cb_command_2)
        QWidget.setTabOrder(self.cb_command_2, self.cb_data_2)
        QWidget.setTabOrder(self.cb_data_2, self.le_check_2)
        QWidget.setTabOrder(self.le_check_2, self.cb_end_2)
        QWidget.setTabOrder(self.cb_end_2, self.pb_preset_2)
        QWidget.setTabOrder(self.pb_preset_2, self.pb_send_2)
        QWidget.setTabOrder(self.pb_send_2, self.cb_start_3)
        QWidget.setTabOrder(self.cb_start_3, self.le_length_3)
        QWidget.setTabOrder(self.le_length_3, self.cb_command_3)
        QWidget.setTabOrder(self.cb_command_3, self.cb_data_3)
        QWidget.setTabOrder(self.cb_data_3, self.le_check_3)
        QWidget.setTabOrder(self.le_check_3, self.cb_end_3)
        QWidget.setTabOrder(self.cb_end_3, self.pb_preset_3)
        QWidget.setTabOrder(self.pb_preset_3, self.pb_send_3)
        QWidget.setTabOrder(self.pb_send_3, self.cb_start_4)
        QWidget.setTabOrder(self.cb_start_4, self.le_length_4)
        QWidget.setTabOrder(self.le_length_4, self.cb_command_4)
        QWidget.setTabOrder(self.cb_command_4, self.cb_data_4)
        QWidget.setTabOrder(self.cb_data_4, self.le_check_4)
        QWidget.setTabOrder(self.le_check_4, self.cb_end_4)
        QWidget.setTabOrder(self.cb_end_4, self.pb_preset_4)
        QWidget.setTabOrder(self.pb_preset_4, self.pb_send_4)
        QWidget.setTabOrder(self.pb_send_4, self.cb_start_5)
        QWidget.setTabOrder(self.cb_start_5, self.le_length_5)
        QWidget.setTabOrder(self.le_length_5, self.cb_command_5)
        QWidget.setTabOrder(self.cb_command_5, self.cb_data_5)
        QWidget.setTabOrder(self.cb_data_5, self.le_check_5)
        QWidget.setTabOrder(self.le_check_5, self.cb_end_5)
        QWidget.setTabOrder(self.cb_end_5, self.pb_preset_5)
        QWidget.setTabOrder(self.pb_preset_5, self.pb_send_5)
        QWidget.setTabOrder(self.pb_send_5, self.le_profile_file)
        QWidget.setTabOrder(self.le_profile_file, self.minimizeAppBtn)
        QWidget.setTabOrder(self.minimizeAppBtn, self.pb_load_profile)
        QWidget.setTabOrder(self.pb_load_profile, self.tableView)
        QWidget.setTabOrder(self.tableView, self.pb_save_profile)
        QWidget.setTabOrder(self.pb_save_profile, self.cb_server_ip)
        QWidget.setTabOrder(self.cb_server_ip, self.pb_export_table)
        QWidget.setTabOrder(self.pb_export_table, self.maximizeRestoreAppBtn)
        QWidget.setTabOrder(self.maximizeRestoreAppBtn, self.closeAppBtn)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.cb_command_1.setCurrentIndex(0)
        self.cb_command_2.setCurrentIndex(1)
        self.cb_command_3.setCurrentIndex(2)
        self.cb_command_4.setCurrentIndex(2)
        self.cb_command_5.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MiaowDaq - ULM7606 Data Acquisition Application", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"MiaowSim", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"A lower machine server", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_connection.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.btn_divider.setText(QCoreApplication.translate("MainWindow", u"Divider", None))
        self.btn_valvedata.setText(QCoreApplication.translate("MainWindow", u"Valve Data", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>MiaowSim - Uppermachine Simulator</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.le_profile_file.setText(QCoreApplication.translate("MainWindow", u"./settings.json", None))
        self.le_profile_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Default to ./profile.json", None))
        self.pb_load_profile.setText(QCoreApplication.translate("MainWindow", u"Load...", None))
        self.pb_save_profile.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"Load or save the specification", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"SPECIFICATION", None))
        self.lbl_server_ip.setText(QCoreApplication.translate("MainWindow", u"Server IP", None))
        self.lbl_server_port.setText(QCoreApplication.translate("MainWindow", u"Server Port", None))
        self.labelBoxBlenderInstalation_4.setText(QCoreApplication.translate("MainWindow", u"MANUAL", None))
        self.cb_end_3.setItemText(0, QCoreApplication.translate("MainWindow", u"BB", None))

        self.cb_end_3.setCurrentText(QCoreApplication.translate("MainWindow", u"BB", None))
        self.cb_data_5.setItemText(0, QCoreApplication.translate("MainWindow", u"FF", None))

        self.cb_data_5.setCurrentText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.lbl_data.setText(QCoreApplication.translate("MainWindow", u"Data (Hex)", None))
        self.lbl_start.setText(QCoreApplication.translate("MainWindow", u"Start (Hex)", None))
        self.cb_start_3.setItemText(0, QCoreApplication.translate("MainWindow", u"AA", None))

        self.cb_start_3.setCurrentText(QCoreApplication.translate("MainWindow", u"AA", None))
#if QT_CONFIG(tooltip)
        self.pb_preset_2.setToolTip(QCoreApplication.translate("MainWindow", u"Add to custom commands", None))
#endif // QT_CONFIG(tooltip)
        self.pb_preset_2.setText("")
        self.cb_start_2.setItemText(0, QCoreApplication.translate("MainWindow", u"AA", None))

        self.cb_start_2.setCurrentText(QCoreApplication.translate("MainWindow", u"AA", None))
        self.lbl_check.setText(QCoreApplication.translate("MainWindow", u"Chk (Hex)", None))
        self.cb_end_1.setItemText(0, QCoreApplication.translate("MainWindow", u"BB", None))

        self.cb_data_2.setItemText(0, QCoreApplication.translate("MainWindow", u"FF", None))

        self.cb_data_2.setCurrentText(QCoreApplication.translate("MainWindow", u"FF", None))
#if QT_CONFIG(tooltip)
        self.pb_send_4.setToolTip(QCoreApplication.translate("MainWindow", u"Send", None))
#endif // QT_CONFIG(tooltip)
        self.pb_send_4.setText("")
#if QT_CONFIG(tooltip)
        self.pb_send_5.setToolTip(QCoreApplication.translate("MainWindow", u"Send", None))
#endif // QT_CONFIG(tooltip)
        self.pb_send_5.setText("")
#if QT_CONFIG(tooltip)
        self.pb_preset_3.setToolTip(QCoreApplication.translate("MainWindow", u"Add to custom commands", None))
#endif // QT_CONFIG(tooltip)
        self.pb_preset_3.setText("")
        self.cb_end_2.setItemText(0, QCoreApplication.translate("MainWindow", u"BB", None))

        self.cb_end_2.setCurrentText(QCoreApplication.translate("MainWindow", u"BB", None))
#if QT_CONFIG(tooltip)
        self.pb_preset_1.setToolTip(QCoreApplication.translate("MainWindow", u"Add to custom commands", None))
#endif // QT_CONFIG(tooltip)
        self.pb_preset_1.setText("")
        self.cb_start_1.setItemText(0, QCoreApplication.translate("MainWindow", u"AA", None))

        self.cb_start_5.setItemText(0, QCoreApplication.translate("MainWindow", u"AA", None))

#if QT_CONFIG(tooltip)
        self.pb_send_1.setToolTip(QCoreApplication.translate("MainWindow", u"Send", None))
#endif // QT_CONFIG(tooltip)
        self.pb_send_1.setText("")
        self.cb_end_5.setItemText(0, QCoreApplication.translate("MainWindow", u"BB", None))

#if QT_CONFIG(tooltip)
        self.pb_preset_4.setToolTip(QCoreApplication.translate("MainWindow", u"Add to custom commands", None))
#endif // QT_CONFIG(tooltip)
        self.pb_preset_4.setText("")
        self.cb_data_4.setItemText(0, QCoreApplication.translate("MainWindow", u"FF", None))

        self.cb_data_4.setCurrentText(QCoreApplication.translate("MainWindow", u"FF", None))
#if QT_CONFIG(tooltip)
        self.pb_send_2.setToolTip(QCoreApplication.translate("MainWindow", u"Send", None))
#endif // QT_CONFIG(tooltip)
        self.pb_send_2.setText("")
#if QT_CONFIG(tooltip)
        self.pb_send_3.setToolTip(QCoreApplication.translate("MainWindow", u"Send", None))
#endif // QT_CONFIG(tooltip)
        self.pb_send_3.setText("")
        self.cb_data_3.setItemText(0, QCoreApplication.translate("MainWindow", u"FF", None))

        self.cb_data_3.setCurrentText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.lbl_stop.setText(QCoreApplication.translate("MainWindow", u"End (Hex)", None))
        self.cb_end_4.setItemText(0, QCoreApplication.translate("MainWindow", u"BB", None))

        self.cb_data_1.setItemText(0, QCoreApplication.translate("MainWindow", u"FF", None))

        self.cb_data_1.setCurrentText(QCoreApplication.translate("MainWindow", u"FF", None))
        self.cb_start_4.setItemText(0, QCoreApplication.translate("MainWindow", u"AA", None))

#if QT_CONFIG(tooltip)
        self.pb_preset_5.setToolTip(QCoreApplication.translate("MainWindow", u"Add to custom commands", None))
#endif // QT_CONFIG(tooltip)
        self.pb_preset_5.setText("")
        self.cb_command_1.setItemText(0, QCoreApplication.translate("MainWindow", u"st", None))
        self.cb_command_1.setItemText(1, QCoreApplication.translate("MainWindow", u"sp", None))
        self.cb_command_1.setItemText(2, QCoreApplication.translate("MainWindow", u"te", None))

        self.lbl_command.setText(QCoreApplication.translate("MainWindow", u"Cmd (Str)", None))
        self.lbl_length.setText(QCoreApplication.translate("MainWindow", u"Len (Dec)", None))
        self.cb_command_2.setItemText(0, QCoreApplication.translate("MainWindow", u"st", None))
        self.cb_command_2.setItemText(1, QCoreApplication.translate("MainWindow", u"sp", None))
        self.cb_command_2.setItemText(2, QCoreApplication.translate("MainWindow", u"te", None))

        self.cb_command_2.setCurrentText(QCoreApplication.translate("MainWindow", u"sp", None))
        self.cb_command_3.setItemText(0, QCoreApplication.translate("MainWindow", u"st", None))
        self.cb_command_3.setItemText(1, QCoreApplication.translate("MainWindow", u"sp", None))
        self.cb_command_3.setItemText(2, QCoreApplication.translate("MainWindow", u"te", None))

        self.cb_command_3.setCurrentText(QCoreApplication.translate("MainWindow", u"te", None))
        self.cb_command_4.setItemText(0, QCoreApplication.translate("MainWindow", u"st", None))
        self.cb_command_4.setItemText(1, QCoreApplication.translate("MainWindow", u"sp", None))
        self.cb_command_4.setItemText(2, QCoreApplication.translate("MainWindow", u"te", None))

        self.cb_command_5.setItemText(0, QCoreApplication.translate("MainWindow", u"st", None))
        self.cb_command_5.setItemText(1, QCoreApplication.translate("MainWindow", u"sp", None))
        self.cb_command_5.setItemText(2, QCoreApplication.translate("MainWindow", u"te", None))

        self.labelBoxBlenderInstalation_5.setText(QCoreApplication.translate("MainWindow", u"PRESET", None))
        self.btn_preset_previous.setText("")
        self.le_preset_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_preset_next.setText("")
        self.le_preset_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.btn_preset_add.setText("")
        self.pb_send_camera_a.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.pb_send_camera_b.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.pb_send_camera_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pb_send_camera_d.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pb_send_valve.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.cb_from_camera.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.cb_from_camera.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.cb_from_camera.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.cb_from_camera.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))

        self.cb_from_camera.setCurrentText(QCoreApplication.translate("MainWindow", u"A", None))
        self.le_to_valve.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.pb_send_to_valve.setText(QCoreApplication.translate("MainWindow", u"T", None))
#if QT_CONFIG(tooltip)
        self.pb_divider_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Restore dividers", None))
#endif // QT_CONFIG(tooltip)
        self.pb_divider_restore.setText("")
#if QT_CONFIG(tooltip)
        self.pb_divider_random.setToolTip(QCoreApplication.translate("MainWindow", u"Fill random values", None))
#endif // QT_CONFIG(tooltip)
        self.pb_divider_random.setText("")
#if QT_CONFIG(tooltip)
        self.pb_send_camera_all.setToolTip(QCoreApplication.translate("MainWindow", u"Send all values", None))
#endif // QT_CONFIG(tooltip)
        self.pb_send_camera_all.setText("")
        self.labelBoxBlenderInstalation_6.setText(QCoreApplication.translate("MainWindow", u"PACKETS", None))
        self.pb_send_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pb_send_start_2.setText("")
        self.pb_send_stop.setText("")
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"CAPTURED DATA", None))
        self.pb_export_table.setText(QCoreApplication.translate("MainWindow", u"Export...", None))
        self.lbl_server_addr.setText(QCoreApplication.translate("MainWindow", u"0.0.0.0:0", None))
        self.label_2.setText("")
        self.lbl_client_addr.setText(QCoreApplication.translate("MainWindow", u"0.0.0.0:0", None))
        self.lbl_datagram.setText("")
        self.label_1.setText("")
        self.lbl_tx_count.setText(QCoreApplication.translate("MainWindow", u"0 bytes | 0 packets", None))
        self.label_3.setText("")
        self.lbl_rx_count.setText(QCoreApplication.translate("MainWindow", u"0 bytes | 0 packets", None))
        self.lbl_version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi


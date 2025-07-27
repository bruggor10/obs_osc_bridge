# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledAVXbZL.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(310, 330)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 58, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 71, 21))
        self.sender_ip = QLineEdit(self.centralwidget)
        self.sender_ip.setObjectName(u"sender_ip")
        self.sender_ip.setGeometry(QRect(100, 60, 113, 22))
        self.sender_port = QLineEdit(self.centralwidget)
        self.sender_port.setObjectName(u"sender_port")
        self.sender_port.setGeometry(QRect(220, 60, 51, 22))
        self.receiver_port = QLineEdit(self.centralwidget)
        self.receiver_port.setObjectName(u"receiver_port")
        self.receiver_port.setGeometry(QRect(100, 30, 171, 22))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 120, 101, 16))
        self.obs_ip = QLineEdit(self.centralwidget)
        self.obs_ip.setObjectName(u"obs_ip")
        self.obs_ip.setGeometry(QRect(40, 140, 161, 22))
        self.obs_port = QLineEdit(self.centralwidget)
        self.obs_port.setObjectName(u"obs_port")
        self.obs_port.setGeometry(QRect(210, 140, 51, 22))
        self.obs_pass = QLineEdit(self.centralwidget)
        self.obs_pass.setObjectName(u"obs_pass")
        self.obs_pass.setGeometry(QRect(40, 170, 221, 22))
        self.obs_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.connect_btn = QPushButton(self.centralwidget)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setGeometry(QRect(40, 200, 221, 23))
        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(40, 260, 101, 23))
        self.load_btn = QPushButton(self.centralwidget)
        self.load_btn.setObjectName(u"load_btn")
        self.load_btn.setGeometry(QRect(160, 260, 101, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 310, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.receiver_port, self.sender_ip)
        QWidget.setTabOrder(self.sender_ip, self.sender_port)
        QWidget.setTabOrder(self.sender_port, self.obs_ip)
        QWidget.setTabOrder(self.obs_ip, self.obs_port)
        QWidget.setTabOrder(self.obs_port, self.obs_pass)
        QWidget.setTabOrder(self.obs_pass, self.connect_btn)
        QWidget.setTabOrder(self.connect_btn, self.save_btn)
        QWidget.setTabOrder(self.save_btn, self.load_btn)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OBS OSC Bridge", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Osc Input", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Osc Output", None))
        self.sender_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ip Address", None))
        self.sender_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.receiver_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"OBS Websocket", None))
        self.obs_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ip Adresse", None))
        self.obs_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.obs_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save settings", None))
        self.load_btn.setText(QCoreApplication.translate("MainWindow", u"Load settings", None))
    # retranslateUi


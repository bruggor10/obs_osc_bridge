# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledRpndme.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(555, 368)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 160, 181, 89))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.model_type_classifiers = QRadioButton(self.groupBox)
        self.model_type_classifiers.setObjectName(u"model_type_classifiers")

        self.verticalLayout.addWidget(self.model_type_classifiers)

        self.model_type_regressors = QRadioButton(self.groupBox)
        self.model_type_regressors.setObjectName(u"model_type_regressors")
        self.model_type_regressors.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.verticalLayout.addWidget(self.model_type_regressors)

        self.models = QComboBox(self.centralwidget)
        self.models.setObjectName(u"models")
        self.models.setGeometry(QRect(10, 250, 181, 31))
        self.data_in_blink = QLabel(self.centralwidget)
        self.data_in_blink.setObjectName(u"data_in_blink")
        self.data_in_blink.setGeometry(QRect(270, 20, 21, 21))
        self.data_in_blink.setAutoFillBackground(False)
        self.data_in_blink.setStyleSheet(u"background-color: rgb(246, 97, 81);\n"
"border-color: rgb(119, 118, 123);\n"
"border-radius: 10px;\n"
"border: 2px solid;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 58, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 71, 21))
        self.data_out_blink = QLabel(self.centralwidget)
        self.data_out_blink.setObjectName(u"data_out_blink")
        self.data_out_blink.setGeometry(QRect(270, 50, 21, 21))
        self.data_out_blink.setAutoFillBackground(False)
        self.data_out_blink.setStyleSheet(u"background-color: rgb(246, 97, 81);\n"
"border-color: rgb(119, 118, 123);\n"
"border-radius: 10px;\n"
"border: 2px solid;")
        self.train_btn = QPushButton(self.centralwidget)
        self.train_btn.setObjectName(u"train_btn")
        self.train_btn.setGeometry(QRect(290, 210, 121, 41))
        self.model_trainingstatus = QLabel(self.centralwidget)
        self.model_trainingstatus.setObjectName(u"model_trainingstatus")
        self.model_trainingstatus.setGeometry(QRect(420, 220, 21, 21))
        self.model_trainingstatus.setAutoFillBackground(False)
        self.model_trainingstatus.setStyleSheet(u"background-color: rgb(246, 97, 81);\n"
"border-color: rgb(119, 118, 123);\n"
"border-radius: 10px;\n"
"border: 2px solid;")
        self.record_btn = QPushButton(self.centralwidget)
        self.record_btn.setObjectName(u"record_btn")
        self.record_btn.setGeometry(QRect(290, 160, 121, 41))
        self.record_btn.setCheckable(False)
        self.rec_status = QLabel(self.centralwidget)
        self.rec_status.setObjectName(u"rec_status")
        self.rec_status.setGeometry(QRect(420, 170, 20, 21))
        self.rec_status.setAutoFillBackground(False)
        self.rec_status.setStyleSheet(u"background-color: rgb(246, 97, 81);\n"
"border-color: rgb(119, 118, 123);\n"
"border-radius: 10px;\n"
"border: 2px solid;")
        self.model_runstatus = QLabel(self.centralwidget)
        self.model_runstatus.setObjectName(u"model_runstatus")
        self.model_runstatus.setGeometry(QRect(420, 270, 20, 21))
        self.model_runstatus.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.model_runstatus.setAutoFillBackground(False)
        self.model_runstatus.setStyleSheet(u"background-color: rgb(246, 97, 81);\n"
"border-color: rgb(119, 118, 123);\n"
"border-radius: 10px;\n"
"border: 2px solid;")
        self.run_btn = QPushButton(self.centralwidget)
        self.run_btn.setObjectName(u"run_btn")
        self.run_btn.setGeometry(QRect(290, 260, 120, 41))
        self.run_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.run_btn.setCheckable(False)
        self.sender_ip = QLineEdit(self.centralwidget)
        self.sender_ip.setObjectName(u"sender_ip")
        self.sender_ip.setGeometry(QRect(90, 50, 113, 22))
        self.sender_port = QLineEdit(self.centralwidget)
        self.sender_port.setObjectName(u"sender_port")
        self.sender_port.setGeometry(QRect(210, 50, 51, 22))
        self.receiver_port = QLineEdit(self.centralwidget)
        self.receiver_port.setObjectName(u"receiver_port")
        self.receiver_port.setGeometry(QRect(90, 20, 171, 22))
        self.connect_btn = QPushButton(self.centralwidget)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setGeometry(QRect(20, 80, 261, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 555, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"W\u00e4hle Art des Modelles", None))
        self.model_type_classifiers.setText(QCoreApplication.translate("MainWindow", u"Klassifikatoren", None))
        self.model_type_regressors.setText(QCoreApplication.translate("MainWindow", u"Regressoren", None))
        self.data_in_blink.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Osc Input", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Osc Output", None))
        self.data_out_blink.setText("")
        self.train_btn.setText(QCoreApplication.translate("MainWindow", u"Modell trainieren", None))
        self.model_trainingstatus.setText("")
        self.record_btn.setText(QCoreApplication.translate("MainWindow", u"Daten aufnehmen", None))
        self.rec_status.setText("")
        self.model_runstatus.setText("")
        self.run_btn.setText(QCoreApplication.translate("MainWindow", u"Ausf\u00fchren", None))
        self.sender_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ip Adresse", None))
        self.sender_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.receiver_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"Verbinden", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appUIKkdmUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySimpleGUIQt import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(945, 689)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 25px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-4, 2, 931, 150))
        font = QFont()
        font.setFamily(u"LEIXO")
        font.setPointSize(75)
        font.setUnderline(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"\n"
"}")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.button_close = QPushButton(self.dropShadowFrame)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(893, 15, 20, 20))
        self.button_close.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,100,100);\n"
"}")
        
        self.button_close_2 = QPushButton(self.dropShadowFrame)
        self.button_close_2.setObjectName(u"button_close_2")
        self.button_close_2.setGeometry(QRect(858, 15, 20, 20))
        self.button_close_2.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,255,100);\n"
"}")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"PROJECT IDEAS", None))
        self.button_close.setText("")
        self.button_close_2.setText("")
    # retranslateUi


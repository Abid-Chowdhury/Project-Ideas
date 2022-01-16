# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appUILqRGfh.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 680)
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
        
        # Title
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-4, 2, 931, 141))
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
        
        # Close 
        self.button_close = QPushButton(self.dropShadowFrame)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(885, 15, 20, 20))
        self.button_close.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,100,100);\n"
"}")
        
        # Minimize 
        self.button_minimize = QPushButton(self.dropShadowFrame)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setGeometry(QRect(850, 15, 20, 20))
        self.button_minimize.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,255,100);\n"
"}")
        
        # To Do List
        self.button_to_do_list = QPushButton(self.dropShadowFrame)
        self.button_to_do_list.setObjectName(u"button_to_do_list")
        self.button_to_do_list.setGeometry(QRect(15, 140, 169, 160))
        font1 = QFont()
        font1.setFamily(u"Adam Medium")
        font1.setPointSize(40)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setKerning(False)
        self.button_to_do_list.setFont(font1)
        self.button_to_do_list.setLayoutDirection(Qt.LeftToRight)
        self.button_to_do_list.setAutoFillBackground(False)
        self.button_to_do_list.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_to_do_list.setCheckable(False)
        self.button_to_do_list.setFlat(False)
        
        # Notes
        self.button_notes = QPushButton(self.dropShadowFrame)
        self.button_notes.setObjectName(u"button_notes")
        self.button_notes.setGeometry(QRect(195, 140, 169, 160))
        self.button_notes.setFont(font1)
        self.button_notes.setLayoutDirection(Qt.LeftToRight)
        self.button_notes.setAutoFillBackground(False)
        self.button_notes.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_notes.setCheckable(False)
        self.button_notes.setFlat(False)
        
        # Calendar
        self.button_calender = QPushButton(self.dropShadowFrame)
        self.button_calender.setObjectName(u"button_calender")
        self.button_calender.setGeometry(QRect(375, 140, 169, 160))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_calender.sizePolicy().hasHeightForWidth())
        self.button_calender.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Adam Medium")
        font2.setPointSize(40)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setKerning(False)
        self.button_calender.setFont(font2)
        self.button_calender.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_calender.setLayoutDirection(Qt.LeftToRight)
        self.button_calender.setAutoFillBackground(False)
        self.button_calender.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_calender.setCheckable(False)
        self.button_calender.setFlat(False)
        
        # Chat System
        self.button_chat_system = QPushButton(self.dropShadowFrame)
        self.button_chat_system.setObjectName(u"button_chat_system")
        self.button_chat_system.setGeometry(QRect(555, 140, 169, 160))
        sizePolicy.setHeightForWidth(self.button_chat_system.sizePolicy().hasHeightForWidth())
        self.button_chat_system.setSizePolicy(sizePolicy)
        self.button_chat_system.setFont(font2)
        self.button_chat_system.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_chat_system.setLayoutDirection(Qt.LeftToRight)
        self.button_chat_system.setAutoFillBackground(False)
        self.button_chat_system.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_chat_system.setCheckable(False)
        self.button_chat_system.setFlat(False)
        
        # Weather
        self.button_weather = QPushButton(self.dropShadowFrame)
        self.button_weather.setObjectName(u"button_weather")
        self.button_weather.setGeometry(QRect(735, 140, 169, 160))
        sizePolicy.setHeightForWidth(self.button_weather.sizePolicy().hasHeightForWidth())
        self.button_weather.setSizePolicy(sizePolicy)
        self.button_weather.setFont(font2)
        self.button_weather.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_weather.setLayoutDirection(Qt.LeftToRight)
        self.button_weather.setAutoFillBackground(False)
        self.button_weather.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_weather.setCheckable(False)
        self.button_weather.setFlat(False)
        
        # Portfolio Website
        self.button_portfolio_website = QPushButton(self.dropShadowFrame)
        self.button_portfolio_website.setObjectName(u"button_portfolio_website")
        self.button_portfolio_website.setGeometry(QRect(15, 315, 169, 160))
        self.button_portfolio_website.setFont(font1)
        self.button_portfolio_website.setLayoutDirection(Qt.LeftToRight)
        self.button_portfolio_website.setAutoFillBackground(False)
        self.button_portfolio_website.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_portfolio_website.setCheckable(False)
        self.button_portfolio_website.setFlat(False)
        
        # Netflix Clone
        self.button_netflix_clone = QPushButton(self.dropShadowFrame)
        self.button_netflix_clone.setObjectName(u"button_netflix_clone")
        self.button_netflix_clone.setGeometry(QRect(195, 315, 169, 160))
        self.button_netflix_clone.setFont(font1)
        self.button_netflix_clone.setLayoutDirection(Qt.LeftToRight)
        self.button_netflix_clone.setAutoFillBackground(False)
        self.button_netflix_clone.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_netflix_clone.setCheckable(False)
        self.button_netflix_clone.setFlat(False)
        
        # Chess Game
        self.button_chess_game = QPushButton(self.dropShadowFrame)
        self.button_chess_game.setObjectName(u"button_chess_game")
        self.button_chess_game.setGeometry(QRect(375, 315, 169, 160))
        sizePolicy.setHeightForWidth(self.button_chess_game.sizePolicy().hasHeightForWidth())
        self.button_chess_game.setSizePolicy(sizePolicy)
        self.button_chess_game.setFont(font2)
        self.button_chess_game.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_chess_game.setLayoutDirection(Qt.LeftToRight)
        self.button_chess_game.setAutoFillBackground(False)
        self.button_chess_game.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_chess_game.setCheckable(False)
        self.button_chess_game.setFlat(False)
        
        # Donation Website
        self.button_donation_website = QPushButton(self.dropShadowFrame)
        self.button_donation_website.setObjectName(u"button_donation_website")
        self.button_donation_website.setGeometry(QRect(555, 315, 169, 160))
        sizePolicy.setHeightForWidth(self.button_donation_website.sizePolicy().hasHeightForWidth())
        self.button_donation_website.setSizePolicy(sizePolicy)
        self.button_donation_website.setFont(font2)
        self.button_donation_website.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_donation_website.setLayoutDirection(Qt.LeftToRight)
        self.button_donation_website.setAutoFillBackground(False)
        self.button_donation_website.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_donation_website.setCheckable(False)
        self.button_donation_website.setFlat(False)
        
        # Budget Tracker
        self.button_budget_tracker = QPushButton(self.dropShadowFrame)
        self.button_budget_tracker.setObjectName(u"button_budget_tracker")
        self.button_budget_tracker.setGeometry(QRect(735, 315, 169, 160))
        sizePolicy.setHeightForWidth(self.button_budget_tracker.sizePolicy().hasHeightForWidth())
        self.button_budget_tracker.setSizePolicy(sizePolicy)
        self.button_budget_tracker.setFont(font2)
        self.button_budget_tracker.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_budget_tracker.setLayoutDirection(Qt.LeftToRight)
        self.button_budget_tracker.setAutoFillBackground(False)
        self.button_budget_tracker.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_budget_tracker.setCheckable(False)
        self.button_budget_tracker.setFlat(False)
        
        # Form Validator
        self.button_form_validator = QPushButton(self.dropShadowFrame)
        self.button_form_validator.setObjectName(u"button_form_validator")
        self.button_form_validator.setGeometry(QRect(195, 485, 169, 160))
        self.button_form_validator.setFont(font1)
        self.button_form_validator.setLayoutDirection(Qt.LeftToRight)
        self.button_form_validator.setAutoFillBackground(False)
        self.button_form_validator.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_form_validator.setCheckable(False)
        self.button_form_validator.setFlat(False)
        
        # Stock Trading Bot
        self.button_stock_trading_bot = QPushButton(self.dropShadowFrame)
        self.button_stock_trading_bot.setObjectName(u"button_stock_trading_bot")
        self.button_stock_trading_bot.setGeometry(QRect(555, 485, 169, 160))
        sizePolicy.setHeightForWidth(self.button_stock_trading_bot.sizePolicy().hasHeightForWidth())
        self.button_stock_trading_bot.setSizePolicy(sizePolicy)
        self.button_stock_trading_bot.setFont(font2)
        self.button_stock_trading_bot.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_stock_trading_bot.setLayoutDirection(Qt.LeftToRight)
        self.button_stock_trading_bot.setAutoFillBackground(False)
        self.button_stock_trading_bot.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_stock_trading_bot.setCheckable(False)
        self.button_stock_trading_bot.setFlat(False)
        
        # Web Scraper
        self.button_web_scraper = QPushButton(self.dropShadowFrame)
        self.button_web_scraper.setObjectName(u"button_web_scraper")
        self.button_web_scraper.setGeometry(QRect(375, 485, 169, 160))
        sizePolicy.setHeightForWidth(self.button_web_scraper.sizePolicy().hasHeightForWidth())
        self.button_web_scraper.setSizePolicy(sizePolicy)
        self.button_web_scraper.setFont(font2)
        self.button_web_scraper.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_web_scraper.setLayoutDirection(Qt.LeftToRight)
        self.button_web_scraper.setAutoFillBackground(False)
        self.button_web_scraper.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_web_scraper.setCheckable(False)
        self.button_web_scraper.setFlat(False)
        
        # Tic Tac Toe
        self.button_tic_tac_toe = QPushButton(self.dropShadowFrame)
        self.button_tic_tac_toe.setObjectName(u"button_tic_tac_toe")
        self.button_tic_tac_toe.setGeometry(QRect(15, 485, 169, 160))
        self.button_tic_tac_toe.setFont(font1)
        self.button_tic_tac_toe.setLayoutDirection(Qt.LeftToRight)
        self.button_tic_tac_toe.setAutoFillBackground(False)
        self.button_tic_tac_toe.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_tic_tac_toe.setCheckable(False)
        self.button_tic_tac_toe.setFlat(False)
        
        # Discord Bot
        self.button_discord_bot = QPushButton(self.dropShadowFrame)
        self.button_discord_bot.setObjectName(u"button_discord_bot")
        self.button_discord_bot.setGeometry(QRect(735, 485, 169, 160))
        sizePolicy.setHeightForWidth(self.button_discord_bot.sizePolicy().hasHeightForWidth())
        self.button_discord_bot.setSizePolicy(sizePolicy)
        self.button_discord_bot.setFont(font2)
        self.button_discord_bot.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_discord_bot.setLayoutDirection(Qt.LeftToRight)
        self.button_discord_bot.setAutoFillBackground(False)
        self.button_discord_bot.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 15px;\n"
"}")
        self.button_discord_bot.setCheckable(False)
        self.button_discord_bot.setFlat(False)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    # retranslateUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"PROJECT IDEAS", None))
        self.button_close.setText("")
        self.button_minimize.setText("")
        self.button_to_do_list.setText(QCoreApplication.translate("MainWindow", u"To Do\n"
"List", None))
        self.button_notes.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.button_calender.setText(QCoreApplication.translate("MainWindow", u"Calender", None))
        self.button_chat_system.setText(QCoreApplication.translate("MainWindow", u"Chat\n"
"System", None))
        self.button_weather.setText(QCoreApplication.translate("MainWindow", u"Weather", None))
        self.button_portfolio_website.setText(QCoreApplication.translate("MainWindow", u"Portfolio\n"
"Website", None))
        self.button_netflix_clone.setText(QCoreApplication.translate("MainWindow", u"Netflix\n"
"Clone", None))
        self.button_chess_game.setText(QCoreApplication.translate("MainWindow", u"Chess\n"
"Game", None))
        self.button_donation_website.setText(QCoreApplication.translate("MainWindow", u"Donation\n"
"Website", None))
        self.button_budget_tracker.setText(QCoreApplication.translate("MainWindow", u"Budget\n"
"Tracker", None))
        self.button_form_validator.setText(QCoreApplication.translate("MainWindow", u"Form\n"
"Validator", None))
        self.button_stock_trading_bot.setText(QCoreApplication.translate("MainWindow", u"Stock\n"
"Trading\n"
"Bot", None))
        self.button_web_scraper.setText(QCoreApplication.translate("MainWindow", u"Web\n"
"Scraper", None))
        self.button_tic_tac_toe.setText(QCoreApplication.translate("MainWindow", u"Tic Tac\n"
"Toe", None))
        self.button_discord_bot.setText(QCoreApplication.translate("MainWindow", u"Discord\n"
"Bot", None))
    


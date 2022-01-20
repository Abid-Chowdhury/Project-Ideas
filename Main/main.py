import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from app import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Makes the window rounded and keeps it on top
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)        

        # Move Window
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if Ui_MainWindow.returnStatus() == 1:
                Ui_MainWindow.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.label_title.mouseMoveEvent = moveWindow

        # close/minimize button
        self.ui.button_close.clicked.connect(lambda: self.close())
        self.ui.button_close.clicked.connect(lambda: update_Colors_Txt())
        self.ui.button_minimize.clicked.connect(lambda: self.showMinimized())
        
        # Update Colors.txt
        def update_Colors_Txt():
            buttons = [self.ui.button_to_do_list, 
                       self.ui.button_notes, 
                       self.ui.button_calender,
                       self.ui.button_chat_system,
                       self.ui.button_weather,
                       self.ui.button_portfolio_website,
                       self.ui.button_netflix_clone,
                       self.ui.button_chess_game,
                       self.ui.button_donation_website,
                       self.ui.button_budget_tracker,
                       self.ui.button_tic_tac_toe,
                       self.ui.button_form_validator,
                       self.ui.button_web_scraper,
                       self.ui.button_stock_trading_bot,
                       self.ui.button_discord_bot]

            # gets bg color of button
            # self.ui.button_to_do_list.palette().window().color().name()
            
            for button in buttons:
                print(button.palette().window().color().name())
            
            pass
            
            # FOR EACH BUTTON
                # get color of button
                # set colors.txt to that color
            
        
        # load colors.txt
        def load_Colors_Txt():
            buttons = [self.ui.button_to_do_list, 
                       self.ui.button_notes, 
                       self.ui.button_calender,
                       self.ui.button_chat_system,
                       self.ui.button_weather,
                       self.ui.button_portfolio_website,
                       self.ui.button_netflix_clone,
                       self.ui.button_chess_game,
                       self.ui.button_donation_website,
                       self.ui.button_budget_tracker,
                       self.ui.button_tic_tac_toe,
                       self.ui.button_form_validator,
                       self.ui.button_web_scraper,
                       self.ui.button_stock_trading_bot,
                       self.ui.button_discord_bot]
                        
            colors = open(r'colors.txt', 'r')
            
            for line in colors.readlines():
                for button in buttons:
                    if button.objectName() in line:
                        if 'GRAY' in line:
                            button.setStyleSheet("background-color: #dedede;\n"
                                                 "border-radius: 15px;\n")
                        elif 'YELLOW' in line:
                            button.setStyleSheet("background-color: #ffff64;\n"
                                                 "border-radius: 15px;\n")
                        elif 'GREEN' in line:
                            button.setStyleSheet("background-color: #64ff64;\n"
                                                 "border-radius: 15px;\n")
        
        # buttons
        def change_color(button):
            if button.palette().button().color().name() == '#dedede':
                button.setStyleSheet("background-color: #ffff64;\n"
                                                    "border-radius: 15px;\n")
                
            elif button.palette().button().color().name() == '#ffff64':
                button.setStyleSheet("background-color: #64ff64;\n"
                                                    "border-radius: 15px;\n")

            else:
                button.setStyleSheet("background-color: #dedede;"
                                                        "border-radius: 15px;")

        self.ui.button_to_do_list.clicked.connect(lambda: change_color(self.ui.button_to_do_list))
        self.ui.button_notes.clicked.connect(lambda: change_color(self.ui.button_notes))
        self.ui.button_calender.clicked.connect(lambda: change_color(self.ui.button_calender))
        self.ui.button_chat_system.clicked.connect(lambda: change_color(self.ui.button_chat_system))
        self.ui.button_weather.clicked.connect(lambda: change_color(self.ui.button_weather))
        self.ui.button_portfolio_website.clicked.connect(lambda: change_color(self.ui.button_portfolio_website))
        self.ui.button_netflix_clone.clicked.connect(lambda: change_color(self.ui.button_netflix_clone))   
        self.ui.button_chess_game.clicked.connect(lambda: change_color(self.ui.button_chess_game))
        self.ui.button_donation_website.clicked.connect(lambda: change_color(self.ui.button_donation_website))
        self.ui.button_budget_tracker.clicked.connect(lambda: change_color(self.ui.button_budget_tracker))
        self.ui.button_tic_tac_toe.clicked.connect(lambda: change_color(self.ui.button_tic_tac_toe))
        self.ui.button_form_validator.clicked.connect(lambda: change_color(self.ui.button_form_validator))
        self.ui.button_web_scraper.clicked.connect(lambda: change_color(self.ui.button_web_scraper))
        self.ui.button_stock_trading_bot.clicked.connect(lambda: change_color(self.ui.button_stock_trading_bot))
        self.ui.button_discord_bot.clicked.connect(lambda: change_color(self.ui.button_discord_bot))        
                
        load_Colors_Txt()
        self.show()
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
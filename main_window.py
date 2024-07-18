import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
from main_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()  # Define a signal for logout

    def __init__(self, user, db_manager):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.user = user
        self.db_manager = db_manager

        self.btnCalendar.clicked.connect(lambda: self.change_page(0))
        self.btnAddProject.clicked.connect(lambda: self.change_page(1))
        self.btnAddMachine.clicked.connect(lambda: self.change_page(2))
        self.btnLogout.clicked.connect(self.logout)

    def change_page(self, index):
        self.stackedWidget_2.setCurrentIndex(index)

    def logout(self):
        self.close()
        self.logout_signal.emit()  # Emit the logout signal

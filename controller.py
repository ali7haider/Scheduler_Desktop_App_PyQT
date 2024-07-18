from PyQt5.QtCore import pyqtSignal, QObject
from login import LoginWindow

class Controller(QObject):
    def __init__(self):
        super().__init__()
        self.login_window = None
        self.main_window = None

    def show_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.switch_window.connect(self.show_main_window)
        self.login_window.show()

    def show_main_window(self, user, db_manager):
        from main_window import MainWindow  # Import here to avoid circular import
        self.main_window = MainWindow(user, db_manager)
        self.main_window.logout_signal.connect(self.show_login_window)  # Connect logout signal
        self.main_window.show()
        self.login_window.close()

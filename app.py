import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from login_ui import Ui_MainWindow
from database import DatabaseManager
from main import MainWindow

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.db_manager = DatabaseManager()
        self.db_manager.create_database()

        self.btnOK.clicked.connect(self.loginAuthentication)

    def loginAuthentication(self):
        mail = self.txtMail.text()
        password = self.txtPassword.text()
        user = self.db_manager.authenticate_user(mail, password)

        if user:
            self.openMainScreen(user)
        else:
            self.show_message("Error", "Invalid credentials. Please try again.", QMessageBox.Warning)

    def show_message(self, title, message, icon):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.setStyleSheet("QLabel{color: black;}QPushButton{color: black;border:2px solid black;}")  # Set text color to black
        msg_box.exec_()

    def openMainScreen(self, user):
        self.main_window = MainWindow(user, self.db_manager)
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

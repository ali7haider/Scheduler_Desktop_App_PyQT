import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from login_ui import Ui_MainWindow
from database import DatabaseManager

class LoginWindow(QMainWindow, Ui_MainWindow):
    switch_window = pyqtSignal(object, object)  # Signal to switch window

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.db_manager = DatabaseManager()
        self.db_manager.create_database()
        # self.insert_dummy_data()  # Insert dummy data
        self.btnOK.clicked.connect(self.loginAuthentication)

        # Set QPushButton text color to black
        self.set_button_styles()

    def insert_dummy_data(self):
        self.db_manager.insert_dummy_user('user1@example.com', 'password1')
        self.db_manager.insert_dummy_user('user2@example.com', 'password2')

    def set_button_styles(self):
        self.btnOK.setStyleSheet("QPushButton {color: black;}")

    def loginAuthentication(self):
        mail = self.txtMail.text()
        password = self.txtPassword.text()
        user = self.db_manager.authenticate_user(mail, password)

        if user:
            self.switch_window.emit(user, self.db_manager)  # Emit signal to switch window
        else:
            self.show_message("Error", "Invalid credentials. Please try again.", QMessageBox.Warning)

    def show_message(self, title, message, icon):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.setStyleSheet("QLabel{color: black;}QPushButton{color: black;border:1px solid black;}")  # Set text color to black
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
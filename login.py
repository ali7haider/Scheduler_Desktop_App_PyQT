import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal,Qt
from login_ui import Ui_MainWindow
from database import DatabaseManager
from PyQt5.QtGui import  QMouseEvent

class LoginWindow(QMainWindow, Ui_MainWindow):
    switch_window = pyqtSignal(object, object)  # Signal to switch window

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.db_manager = DatabaseManager()
        self.db_manager.create_tables()
        self.stackedWidget.setCurrentIndex(0)
        # Connect the closeAppBtn button to the close method
        self.closeAppBtn.clicked.connect(self.close)

        # Connect the minimizeAppBtn button to the showMinimized method
        self.minimizeAppBtn.clicked.connect(self.showMinimized)

        self.btnLoginPage.clicked.connect(lambda: self.change_page(0))
        self.btnRegisterPage.clicked.connect(lambda: self.change_page(1))

        self.btnRegister.clicked.connect(self.add_account)




        # self.db_manager.insert_dummy_user("Admin","1234")  # Insert dummy data
        # Set the stylesheet for the btnOK button
        
        self.btnOK.clicked.connect(self.loginAuthentication)

    def add_account(self):
        try:
            mailRegister = self.txtMailRegister.text()
            passwordRegister = self.txtPasswordRegister.text()

            if mailRegister and passwordRegister:
                success = self.db_manager.insert_user(mailRegister, passwordRegister)
                if success:
                    self.show_message("Success", "User added successfully!", QMessageBox.Information)
                    self.txtMailRegister.clear()
                    self.txtPasswordRegister.clear()
                else:
                    self.show_message("Error", "Failed to add user. Please try again. Use other username", QMessageBox.Warning)
            else:
                self.show_message("Error", "Please fill in all fields.", QMessageBox.Warning)
        except Exception as e:
            print(f"An error occurred while adding user: {e}")
            self.show_message("Error", "An unexpected error occurred. Please try again.", QMessageBox.Critical)

    def change_page(self, index):
        self.stackedWidget.setCurrentIndex(index)
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
    # Define the mousePressEvent method to handle mouse button press events
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPos)
            event.accept()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

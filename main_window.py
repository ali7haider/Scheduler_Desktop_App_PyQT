import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from main_ui import Ui_MainWindow
from database import DatabaseManager

class MainWindow(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()  # Define a signal for logout

    def __init__(self, user, db_manager):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.user = user
        self.db_manager = db_manager

        self.btnCalendar.clicked.connect(lambda: self.change_page(0))
        self.btnProject.clicked.connect(lambda: self.change_page(1))
        self.btnMachine.clicked.connect(lambda: self.change_page(2))
        self.btnLogout.clicked.connect(self.logout)

        self.btnAddMachine.clicked.connect(self.add_machine)

    def change_page(self, index):
        self.stackedWidget_2.setCurrentIndex(index)

    def logout(self):
        self.close()
        self.logout_signal.emit()  # Emit the logout signal

    def add_machine(self):
        try:
            machine_name = self.txtMachineName.text()

            technology = self.cmbxTechnology.currentText()

            if machine_name and technology:
                self.db_manager.insert_machine(machine_name, technology)
                self.show_message("Success", "Machine added successfully!", QMessageBox.Information)
                self.reset_fields()
            else:
                self.show_message("Error", "Please fill in all fields.", QMessageBox.Warning)
        except Exception as e:
            print(f"An error occurred: {e}")

    def reset_fields(self):
        self.txtMachineName.clear()
        self.cmbxTechnology.setCurrentIndex(0)

    def show_message(self, title, message, icon):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.setStyleSheet("QLabel{color: black;}QPushButton{color: black;border:1px solid black;}")  # Set text color to black
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    user = None  # Dummy user for testing
    db_manager = DatabaseManager()
    window = MainWindow(user, db_manager)
    window.show()
    sys.exit(app.exec_())

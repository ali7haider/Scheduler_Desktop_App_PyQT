import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_ui import Ui_MainWindow


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        # Set up the user interface from the generated class
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

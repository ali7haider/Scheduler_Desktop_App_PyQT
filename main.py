import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
from database import DatabaseManager

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user, db_manager):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.user = user
        self.db_manager = db_manager
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(None, None)
    window.show()
    sys.exit(app.exec_())

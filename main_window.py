import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal, QDateTime
from main_ui import Ui_MainWindow
from database import DatabaseManager
from datetime import datetime, timedelta


class MainWindow(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()  # Define a signal for logout

    def __init__(self, user, db_manager):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.user = user
        self.db_manager = db_manager
        self.stackedWidget_2.setCurrentIndex(0)
        # Load machines into combo box
        self.load_machines()

        self.load_subject()

        # Load active projects on initialization
        self.load_active_projects()
        self.btnCalendar.clicked.connect(lambda: self.change_page(0))
        self.btnProject.clicked.connect(lambda: self.change_page(1))
        self.btnMachine.clicked.connect(lambda: self.change_page(2))
        self.btnSubject.clicked.connect(lambda: self.change_page(3))

        self.btnLogout.clicked.connect(self.logout)

        self.btnAddMachine.clicked.connect(self.add_machine)
        self.btnCalendar.clicked.connect(self.load_active_projects)

        self.btnAddSubject.clicked.connect(self.add_subject)

        self.btnAddProject.clicked.connect(self.add_project)

        # Set current date and time for dateTimeTemps
        self.dateTimeTemps.setDateTime(QDateTime.currentDateTime())

        

    def load_active_projects(self):
        try:
            projects = self.db_manager.fetch_active_projects()

            if projects:
                # Create HTML to display the list of projects
                html_content = "<h2>Active Projects</h2><ul style='padding-left: 20px;'>"

                for project in projects:
                    project_id, quote_number, date_time, machine_name, subject_name, hours, minutes = project
                    start_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
                    end_time = start_time + timedelta(hours=hours, minutes=minutes)
                    
                    html_content += f"""
                    <li style='margin-bottom: 20px;'>
                        <strong>Quote Number:</strong> {quote_number}<br>
                        <strong>Start Time:</strong> {start_time.strftime("%Y-%m-%d %H:%M:%S")}<br>
                        <strong>End Time:</strong> {end_time.strftime("%Y-%m-%d %H:%M:%S")}<br>
                        <strong>Machine:</strong> {machine_name}<br>
                        <strong>Subject:</strong> {subject_name}<br>
                        <strong>Duration:</strong> {hours} hours {minutes} minutes
                    </li>
                    """

                html_content += "</ul>"
                self.txtCalendar.setHtml(html_content)  # Ensure txtCalendar is a QTextEdit
            else:
                self.txtCalendar.setHtml("<p>No active projects found.</p>")
        except Exception as e:
            print(f"An error occurred while loading active projects: {e}")


    def change_page(self, index):
        self.stackedWidget_2.setCurrentIndex(index)

    def logout(self):
        self.close()
        self.logout_signal.emit()  # Emit the logout signal

    def add_subject(self):
        try:
            subject_name = self.txtSubject.text()
            if subject_name:
                self.db_manager.insert_subject(subject_name)
                self.show_message("Success", "Subject added successfully!", QMessageBox.Information)
                self.reset_fields()
                self.load_subject()

            else:
                self.show_message("Error", "Please fill in all fields.", QMessageBox.Warning)
        except Exception as e:
            print(f"An error occurred while adding subject: {e}")
    def add_machine(self):
        try:
            machine_name = self.txtMachineName.text()
            technology = self.cmbxTechnology.currentText()

            if machine_name and technology:
                self.db_manager.insert_machine(machine_name, technology)
                self.show_message("Success", "Machine added successfully!", QMessageBox.Information)
                self.reset_fields()
                self.load_machines()

            else:
                self.show_message("Error", "Please fill in all fields.", QMessageBox.Warning)
        except Exception as e:
            print(f"An error occurred while adding machine: {e}")

    def add_project(self):
        try:
            quote_number = self.txtQuoteNumber.text()
            machine = self.cmbxMachines.currentText()
            subject = self.cmbxSubjects.currentText()

            date_time = self.dateTimeTemps.dateTime().toString("yyyy-MM-dd HH:mm:ss")
            hours = self.txtHours.text()
            minutes = self.txtMinutes.text()

            if quote_number and machine and subject and date_time and hours and minutes:
                self.db_manager.insert_project(quote_number, machine, subject, date_time, hours, minutes)
                self.show_message("Success", "Project added successfully!", QMessageBox.Information)
                self.reset_project_fields()
            else:
                self.show_message("Error", "Please fill in all fields.", QMessageBox.Warning)
        except Exception as e:
            print(f"An error occurred while adding project: {e}")


    def load_machines(self):
        try:
            self.cmbxMachines.clear()  # Clear the combo box first
            machines = self.db_manager.load_machines()
            for machine_id, machine_name in machines:
                self.cmbxMachines.addItem(machine_name, machine_id)
        except Exception as e:
            print(f"An error occurred while loading machines: {e}")

    def load_subject(self):
        try:
            self.cmbxSubjects.clear()  # Clear the combo box first
            subjects = self.db_manager.load_subjects()
            for id, name in subjects:
                self.cmbxSubjects.addItem(name, id)
        except Exception as e:
            print(f"An error occurred while loading subject: {e}")
    def reset_fields(self):
        self.txtMachineName.clear()
        self.txtSubject.clear()
        self.cmbxTechnology.setCurrentIndex(0)

    def reset_project_fields(self):
        self.txtQuoteNumber.clear()
        self.cmbxMachines.setCurrentIndex(0)
        self.cmbxSubjects.setCurrentIndex(0)
        self.dateTimeTemps.setDateTime(QDateTime.currentDateTime())

        self.txtHours.clear()
        self.txtMinutes.clear()

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

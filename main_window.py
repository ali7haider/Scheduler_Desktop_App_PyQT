import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QHeaderView,QPushButton, QMessageBox, QTableWidgetItem, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import pyqtSignal, QDateTime, QDateTime, Qt
from PyQt5.QtGui import QColor, QPalette
from main_ui import Ui_MainWindow
from database import DatabaseManager
from datetime import datetime, timedelta
import sip
from PyQt5.QtGui import  QMouseEvent

class MainWindow(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()  # Define a signal for logout

    def __init__(self, user, db_manager):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Connect the closeAppBtn button to the close method
        self.closeAppBtn.clicked.connect(self.close)

        # Connect the minimizeAppBtn button to the showMinimized method
        self.minimizeAppBtn.clicked.connect(self.showMinimized)

        self.maximizeAppBtn.clicked.connect(self.maximize_window)

        self.user = user
        self.db_manager = db_manager
        self.stackedWidget_2.setCurrentIndex(0)
        self.tableProject.setColumnCount(7)  # Adjust based on your requirements
        self.tableProject.setHorizontalHeaderLabels(["Quote Number", "Start Time", "End Time", "Machine", "Subject", "Duration", "Actions"])

        # Load machines into combo box
        self.load_machines()

        self.load_subject()

        self.btnCalendar.clicked.connect(self.load_active_projects)
        # Load active projects on initialization
        self.load_active_projects()
        self.btnCalendar.clicked.connect(lambda: self.change_page(0))
        self.btnProject.clicked.connect(lambda: self.change_page(1))
        self.btnMachine.clicked.connect(lambda: self.change_page(2))
        self.btnSubject.clicked.connect(lambda: self.change_page(3))
        self.btnVisual.clicked.connect(lambda: self.createVisualGraph())

        self.btnLogout.clicked.connect(self.logout)

        self.btnAddMachine.clicked.connect(self.add_machine)
        self.btnProject.clicked.connect(self.load_active_projects_table)


        self.btnAddSubject.clicked.connect(self.add_subject)

        self.btnAddProject.clicked.connect(self.add_project)

        # Set current date and time for dateTimeTemps
        self.dateTimeTemps.setDateTime(QDateTime.currentDateTime())
        
        self.load_active_projects_table()

        # Weekday name mapping
        self.weekday_mapping = {
            'Monday': 'Lundi',
            'Tuesday': 'Mardi',
            'Wednesday': 'Mercredi',
            'Thursday': 'Jeudi',
            'Friday': 'Vendredi',
            'Saturday': 'Samedi',
            'Sunday': 'Dimanche'
        }

        self.month_mapping = {
            'January': 'Janvier',
            'February': 'Février',
            'March': 'Mars',
            'April': 'Avril',
            'May': 'Mai',
            'June': 'Juin',
            'July': 'Juillet',
            'August': 'Août',
            'September': 'Septembre',
            'October': 'Octobre',
            'November': 'Novembre',
            'December': 'Décembre'
        }

        

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
    def load_active_projects_table(self):
        self.tableProject.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        try:
            projects = self.db_manager.fetch_active_projects()

            # Clear existing data from the table
            self.tableProject.setRowCount(0)
            self.tableProject.setColumnCount(0)
            self.tableProject.horizontalHeader().setVisible(True)
            self.tableProject.verticalHeader().setVisible(True)
            self.tableProject.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


            # Set table column headers
            headers = ["Quote Number", "Start Time", "End Time", "Machine", "Subject", "Duration", "Actions"]
            self.tableProject.setColumnCount(len(headers))
            self.tableProject.setHorizontalHeaderLabels(headers)
            # Apply stylesheet to the header
            self.tableProject.horizontalHeader().setStyleSheet("""
                QHeaderView::section {
                    background-color: #121212;
                    color: rgb(255, 255, 255);
                    font: bold 10pt "Arial";
                    padding: 5px;
                    border: 1px solid #333;  /* Optional: adds a border around header sections */
                }
            """)

            # Apply stylesheet to the cells
            self.tableProject.setStyleSheet("""
                QTableWidget::item {
                    padding: 2px;
                    color:white;
                    border: 1px solid #333;  /* Optional: adds a border around cells */
                }
                QTableWidget::item:selected {
                    background-color: #333; /* Optional: changes background color for selected items */
                    color: #fff;  /* Optional: changes text color for selected items */
                }
        """)
            # Populate the table with data
            for project in projects:
                project_id, quote_number, date_time, machine_name, subject_name, hours, minutes = project
                start_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
                end_time = start_time + timedelta(hours=hours, minutes=minutes)

                row_position = self.tableProject.rowCount()
                self.tableProject.insertRow(row_position)

                self.tableProject.setItem(row_position, 0, QTableWidgetItem(str(quote_number)))
                self.tableProject.setItem(row_position, 1, QTableWidgetItem(start_time.strftime("%Y-%m-%d %H:%M:%S")))
                self.tableProject.setItem(row_position, 2, QTableWidgetItem(end_time.strftime("%Y-%m-%d %H:%M:%S")))
                self.tableProject.setItem(row_position, 3, QTableWidgetItem(machine_name))
                self.tableProject.setItem(row_position, 4, QTableWidgetItem(subject_name))
                self.tableProject.setItem(row_position, 5, QTableWidgetItem(f"{hours} hours {minutes} minutes"))

                delete_button = QPushButton("Delete")
                delete_button.setStyleSheet("""
                    QPushButton {
                        padding: 2px;
                        border-radius: 5px;
                        color: rgb(255, 255, 255);
                        font: bold 10pt "Arial";
                        background-color: #121212;
                        
                    }
                """)
                delete_button.clicked.connect(lambda _, pid=project_id: self.confirm_delete_project(pid))
                self.tableProject.setCellWidget(row_position, 6, delete_button)

            # Resize columns to content
            self.tableProject.resizeColumnsToContents()
        except Exception as e:
            print(f"An error occurred while loading active projects: {e}")
    def confirm_delete_project(self, project_id):
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Warning)
        confirm_dialog.setWindowTitle("Confirm Deletion")
        confirm_dialog.setText("Are you sure you want to delete this project?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)

        if confirm_dialog.exec_() == QMessageBox.Yes:
            self.delete_project(project_id)

    def delete_project(self, project_id):
        try:
            self.db_manager.mark_project_inactive(project_id)
            self.load_active_projects()
            self.load_active_projects_table()
            self.tableProject.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        except Exception as e:
            print(f"An error occurred while deleting the project: {e}")

    # In your db_manager class, add the method to mark the project inactive
    

    def change_page(self, index):
        self.tableProject.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.stackedWidget_2.setCurrentIndex(index)

    def createVisualGraph(self):
        self.change_page(4)

        machine_data = self.db_manager.load_machines()
        machines = [machine[1] for machine in machine_data]
        projects = self.db_manager.fetch_active_projects()

        # Remove the existing layout from the frame
        self.clear_layout(self.frame_7.layout())

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)  # Set spacing between cells to zero
        self.grid_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        self.frame_7.setLayout(self.grid_layout)
        self.set_month_label()
        self.set_grid_headers(machines)
        self.populate_grid(projects, machines)

    def set_month_label(self):
        current_date = datetime.today()
        month_name = current_date.strftime('%B')
        self.lblMonth.setText(f"{self.month_mapping[month_name]}")

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_layout(item.layout())
            sip.delete(layout)

    def set_grid_headers(self, machines):
        # Customize cell backgrounds
        for row in range(len(machines) + 1):
            for col in range(7):
                cell_widget = QWidget()
                cell_widget.setStyleSheet("background-color: #636161" if col % 2 == 0 else "background-color: #4C4C4C")
                cell_widget.setAutoFillBackground(True)
                self.grid_layout.addWidget(cell_widget, row, col+1)

        # Update the current date to start from two days before today
        current_date = datetime.today().date() - timedelta(days=2)
        for col in range(7):
            day = current_date + timedelta(days=col)
            day_label_text = f"{self.weekday_mapping[day.strftime('%A')]} {day.day}"
            day_label = QLabel(day_label_text)
            day_label.setAlignment(Qt.AlignCenter)
            day_label.setStyleSheet("background-color: #636161; color: black; font-weight: bold;" if col % 2 == 0 else "background-color: #4C4C4C; color: black; font-weight: bold;")
            day_label.setAutoFillBackground(True)
            self.grid_layout.addWidget(day_label, 0, col + 1)  # Start from column 1 to leave space for row headers

        total_height = self.frame_7.height()
        row_height = total_height // (len(machines) + 1)  # Divide the height by the number of machines

        for row, machine in enumerate(machines):
            machine_label = QLabel(machine)
            machine_label.setAlignment(Qt.AlignCenter)
            machine_label.setFixedHeight(row_height)  # Set the height
            self.grid_layout.addWidget(machine_label, row + 1, 0)  # Start from row 1 to leave space for column headers

    def populate_grid(self, data, machines):
        machine_colors = [
            (141, 206, 243),
            (244, 158, 154),
            (250, 205, 140),
            (200, 225, 157),
            (254, 249, 157),
            (168, 245, 120),
            (181, 137, 250),
            (237, 145, 214),
            (250, 236, 130),
            (106, 204, 170)
        ]

        # Update the current date to start from two days before today
        current_date = datetime.today().date() - timedelta(days=2)
        for entry in data:
            project_id, quote_number, date_time, machine_name, subject_name, hours, minutes = entry
            start_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
            # Calculate the total duration in seconds
            total_duration = timedelta(hours=hours, minutes=minutes).total_seconds()

            # Calculate end_time by adding total_duration to the date part of start_time
            end_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(seconds=total_duration)

            machine_index = machines.index(machine_name)

            # Calculate start and end columns
            start_column = (start_time.date() - current_date).days
            end_column = (end_time.date() - current_date).days

            if start_column < 0 or end_column >= 7:
                continue  # Skip if out of the current week range

            # Create a label for the entry
            if subject_name == 'Maintenance':
                entry_label = QLabel('Maintenance')
                entry_label.setStyleSheet("QLabel{background-color: rgb(252, 1, 2); color: rgb(0, 0, 0);}")
            else:
                entry_label = QLabel(text= f'DE#{quote_number} FIN:{hours}h{minutes}')
                color = machine_colors[machine_index % len(machine_colors)]
                entry_label.setStyleSheet("QLabel{background-color: rgb" + str(color) + "; color: rgb(0, 0, 0);}")
            entry_label.setAlignment(Qt.AlignCenter)
            entry_label.setFixedHeight(20)  # Set the height to 50
            entry_label.setAutoFillBackground(True)

            # Add the label to the grid, spanning multiple columns if necessary
            self.grid_layout.addWidget(entry_label, machine_index + 1, start_column + 1, 1, end_column - start_column + 1)

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
                self.load_active_projects_table()
                self.tableProject.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

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
    def maximize_window(self):
        # If the window is already maximized, restore it
        if self.isMaximized():
            self.showNormal()
        # Otherwise, maximize it
        else:
            self.showMaximized()
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
    user = None  # Dummy user for testing
    db_manager = DatabaseManager()
    window = MainWindow(user, db_manager)
    window.show()
    sys.exit(app.exec_())

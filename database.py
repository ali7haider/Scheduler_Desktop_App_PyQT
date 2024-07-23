import sqlite3

class DatabaseManager:
    def __init__(self, db_name='DB.db'):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Create the Users table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mail TEXT UNIQUE,
                password TEXT,
                isactive INTEGER DEFAULT 0
            )
        ''')

        # Create the Machines table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Machines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                technology TEXT
            )
        ''')
        # Create the Machines table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        ''')


        # Create the Projects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote_number TEXT,
                machine_id INTEGER,
                subject_id INTEGER,
                datetime TEXT,
                hours INTEGER,
                minutes INTEGER,
                isactive INTEGER DEFAULT 1,
                FOREIGN KEY(machine_id) REFERENCES Machines(id)
                FOREIGN KEY(subject_id) REFERENCES Subjects(id)

            )
        ''')

        conn.commit()
        conn.close()

    def fetch_active_projects(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT p.id, p.quote_number, p.datetime, m.name AS machine_name, s.name AS subject_name, p.hours, p.minutes
            FROM Projects p
            JOIN Machines m ON p.machine_id = m.id
            JOIN Subjects s ON p.subject_id = s.id
            WHERE p.isactive = 1
        ''')

        projects = cursor.fetchall()
        conn.close()

        return projects
    def insert_dummy_user(self, mail, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Users (mail, password, isactive) VALUES (?, ?, ?)
            ''', (mail, password, 1))
            conn.commit()
        except sqlite3.IntegrityError:
            pass
        conn.close()

    def insert_subject(self, name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Subjects (name) VALUES (?)
        ''', (name,))  # Note the comma to create a tuple
        conn.commit()
        conn.close()

    def insert_machine(self, name, technology):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Machines (name, technology) VALUES (?, ?)
        ''', (name, technology))
        conn.commit()
        conn.close()

    def authenticate_user(self, mail, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM Users WHERE mail=? AND password=? AND isactive=1
        ''', (mail, password))
        user = cursor.fetchone()
        conn.close()
        return user


    def insert_dummy_user(self, mail, password):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Users (mail, password, isactive) VALUES (?, ?, ?)', (mail, password, 1))
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error inserting dummy user: {e}")
        finally:
            conn.close()

    def load_machines(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM Machines')
        machines = cursor.fetchall()
        conn.close()
        return machines
    def load_subjects(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM Subjects')
        machines = cursor.fetchall()
        conn.close()
        return machines

    def insert_project(self, quote_number, machine, subject, date_time, hours, minutes):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Get machine_id
        cursor.execute('SELECT id FROM Machines WHERE name = ?', (machine,))
        machine_id = cursor.fetchone()[0]

        # Get subject_id
        cursor.execute('SELECT id FROM Subjects WHERE name = ?', (subject,))
        subject_id = cursor.fetchone()[0]

        # Insert project
        cursor.execute('INSERT INTO Projects (quote_number, machine_id, subject_id, datetime, hours, minutes) VALUES (?, ?, ?, ?, ?, ?)',
                    (quote_number, machine_id, subject_id, date_time, hours, minutes))
        conn.commit()
        conn.close()


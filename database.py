import sqlite3

class DatabaseManager:
    def __init__(self, db_name='DB.db'):
        self.db_name = db_name
        self.create_database()

    def create_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mail TEXT UNIQUE,
                password TEXT,
                isactive INTEGER DEFAULT 0
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Machines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                technology TEXT
            )
        ''')

        conn.commit()
        conn.close()

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

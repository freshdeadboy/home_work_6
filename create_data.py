import sqlite3
from faker import Faker
import random

fake = Faker()

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE,
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    )
    ''')

def populate_tables(cursor, connection):
    groups = ['Group A', 'Group B', 'Group C']
    for group in groups:
        cursor.execute("INSERT INTO groups (name) VALUES (?)", (group,))
    connection.commit()

    teachers = [fake.name() for _ in range(5)]
    for teacher in teachers:
        cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher,))
    connection.commit()

    for _ in range(30):
        name = fake.name()
        group_id = random.randint(1, 3)
        cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))
    connection.commit()

    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History']
    for subject in subjects:
        teacher_id = random.randint(1, 5)
        cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))
    connection.commit()

    for student_id in range(1, 31):
        for subject_id in range(1, 6):
            grade = random.randint(1, 100)
            date = fake.date_of_birth(minimum_age=18, maximum_age=22).strftime('%Y-%m-%d')
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)", (student_id, subject_id, grade, date))
    connection.commit()

def main():
    connection = sqlite3.connect('university.db')
    cursor = connection.cursor()

    create_tables(cursor)
    populate_tables(cursor, connection)

    connection.close()

    print("Базу даних успішно створено та заповнено випадковими даними.")

if __name__ == "__main__":
    main()
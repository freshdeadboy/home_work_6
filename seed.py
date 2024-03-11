from sqlalchemy import func
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade
import random

fake = Faker()

def create_students(session, num_students):
    for _ in range(num_students):
        name = fake.name()
        group = session.query(Group).order_by(func.random()).first()
        student = Student(name=name, group_id=group.id)  
        session.add(student)
    session.commit()

def create_groups(session, num_groups):
    for _ in range(num_groups):
        name = f"Group {chr(65 + _)}"
        group = Group(name=name)
        session.add(group)
    session.commit()

def create_teachers(session, num_teachers):
    for _ in range(num_teachers):
        name = fake.name()
        teacher = Teacher(name=name)
        session.add(teacher)
    session.commit()

def create_subjects(session, num_subjects):
    for _ in range(num_subjects):
        name = fake.word()
        teacher = session.query(Teacher).order_by(func.random()).first()
        subject = Subject(name=name, teacher_id=teacher.id)  
        session.add(subject)
    session.commit()

def create_grades(session, num_grades):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students:
        for subject in subjects:
            for _ in range(num_grades):
                grade_value = random.randint(1, 100)
                date = fake.date_between(start_date='-1y', end_date='today')
                grade = Grade(student_id=student.id, subject_id=subject.id, grade=grade_value, date=date)
                session.add(grade)
    session.commit()

def main():
    engine = create_engine('sqlite:///university.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    num_students = random.randint(30, 50)
    num_groups = 3
    num_teachers = random.randint(3, 5)
    num_subjects = random.randint(5, 8)
    num_grades = 20

    create_groups(session, num_groups)
    create_teachers(session, num_teachers)
    create_students(session, num_students)
    create_subjects(session, num_subjects)
    create_grades(session, num_grades)

    session.close()
    print("Дані успішно згенеровано та збережено в базі даних.")

if __name__ == "__main__":
    main()

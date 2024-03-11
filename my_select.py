from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from models import Student, Grade, Subject, Group, Teacher

engine = create_engine('sqlite:///university.db')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    result = session.query(Student, func.avg(Grade.grade).label('average_grade')) \
                    .join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()) \
                    .limit(5).all()
    return result

def select_2(subject_name):
    result = session.query(Student, func.avg(Grade.grade).label('average_grade')) \
                    .join(Grade).join(Subject) \
                    .filter(Subject.name == subject_name) \
                    .group_by(Student.id).order_by(func.avg(Grade.grade).desc()) \
                    .first()
    return result

def select_3(subject_name):
    with Session() as session:
        result = session.query(func.avg(Grade.grade).label('average_grade')) \
            .join(Subject) \
            .filter(Subject.name == subject_name) \
            .group_by(Subject.name) \
            .all()
    return result

def select_4():
    result = session.query(func.avg(Grade.grade)).scalar()
    return result

def select_5(teacher_name):
    result = session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()
    return result

def select_6(group_name):
    result = session.query(Student.name).join(Group).filter(Group.name == group_name).all()
    return result

def select_7(group_name, subject_name):
    result = session.query(Student.name, Grade.grade) \
                    .join(Group).join(Grade).join(Subject) \
                    .filter(Group.name == group_name, Subject.name == subject_name) \
                    .all()
    return result

def select_8(teacher_name):
    result = session.query(func.avg(Grade.grade)) \
                    .join(Subject).join(Teacher) \
                    .filter(Teacher.name == teacher_name) \
                    .scalar()
    return result

def select_9(student_name):
    result = session.query(Subject.name).join(Grade).join(Student) \
                    .filter(Student.name == student_name).all()
    return result

def select_10(student_name, teacher_name):
    result = session.query(Subject.name) \
                    .join(Grade).join(Student).join(Teacher) \
                    .filter(Student.name == student_name, Teacher.name == teacher_name) \
                    .all()
    return result

if __name__ == "__main__":
    print(select_1())
    print(select_2("Mathematics"))
    print(select_3("Mathematics"))
    print(select_4())
    print(select_5("John Doe"))
    print(select_6("Group A"))
    print(select_7("Group A", "Mathematics"))
    print(select_8("John Doe"))
    print(select_9("Alice Smith"))
    print(select_10("Alice Smith", "John Doe"))

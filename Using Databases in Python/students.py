from peewee import *


db = SqliteDatabase('students.db')


class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)
    
    # Tell the model which database to connect to
    class Meta:
        database = db
        
students = [
    {'username': 'kennethlove',
     'points': 18537},
    {'username': 'chalkers',
     'points': 11912},
    {'username': 'brianweber',
     'points': 18536},
    {'username': 'craigdennis',
     'points': 4879},
    {'username': 'davemcfarland',
     'points': 14717},
]

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError: # if the username already exists
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()
            
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Our top student right now is: {0.username}.".format(top_student()))
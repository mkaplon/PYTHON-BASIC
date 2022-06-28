"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

from datetime import datetime, timedelta
from part2.task_classes import Homework, Student, Teacher
import pytest

@pytest.fixture
def teacher():
    return Teacher("Adam", "Nowak")

@pytest.fixture
def student():
    return Student("Jan", "Kowalski")

#TEACHER

def test_Teacher(teacher):
    assert teacher.first_name == "Adam"
    assert teacher.last_name == "Nowak"

#HOMEWORK

parameters=[
    ("Learn functions", 5),
    ("Create 2 classes", 0),
    ("Create project", -4)
]

@pytest.mark.parametrize('name, days', parameters)
def test_Homework(teacher, name, days):
    homework1 = teacher.create_homework(name, days)
    assert datetime.now() - homework1.created < timedelta(seconds=1)
    assert homework1.deadline == timedelta(days=days)
    assert homework1.text == name

parameters2=[
    ("Learn functions", 5, True),
    ("Create 2 classes", 0, False),
    ("Create project", -4, False)
]

@pytest.mark.parametrize('name, days, is_active', parameters2)
def test_is_active(teacher, name, days, is_active):
    homework1 = teacher.create_homework(name, days)
    assert homework1.is_active() == is_active

#STUDENT

def test_Student(student):
    assert student.first_name == "Jan"
    assert student.last_name == "Kowalski"

def test_do_active_homework(student, teacher):
    homework1 = teacher.create_homework("Active homework", 10)
    assert student.do_homework(homework1) == homework1

def test_do_expired_homework(capfd, student, teacher):
    homework1 = teacher.create_homework("Expired homework", -3)
    student.do_homework(homework1)
    out, err = capfd.readouterr()
    assert out == "You are late!\n"
    assert student.do_homework(homework1) is None

    


    
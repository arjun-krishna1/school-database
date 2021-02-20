from django.db import models

class Person(models.Model):
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

class Professor(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    salary = models.DecimalField(max_digits=8, decimal_places=2)

class Student(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    is_local = models.BooleanField()

class StudentCourseGrade(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(course)
    grade = models.DecimalField(max_digits=3, decimal_places=2)

class Course(models.Model):
    teachers = models.ManyToManyField(Teacher)
    students = models.ManyToManyField(Student, through=StudentCourseGrade)


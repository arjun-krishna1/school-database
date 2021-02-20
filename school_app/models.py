from django.db import models

class Person(models.Model):
    # Parameters
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    # Methods
    def __str__(self):
        return self.name

class Professor(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    BONUS_PAY = 20000

    # Methods
    def __str__(self):
        return "Professor " + self.name

    def get_total_pay():
        # professors get a bonus if they teach more than 4 courses
        pay = self.salary
        courses_taught = Course.objects.filter(teachers_person_pk = self.person.pk)
        
        if len(courses_taught) > 4:
            pay += self.BONUS_PAY

        return pay

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
    min_students = models.IntegerField()
    max_students = models.IntegerField()


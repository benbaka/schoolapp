from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Stage(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)


class AcademicYear(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)


class RollCall(models.Model):
    student = models.ForeignKey(Student)
    academicYear = models.OneToOneField(AcademicYear)
    stage = models.OneToOneField(Stage)
    present = models.BooleanField()
    rollCall_date = models.DateTimeField()

from django.db import models


# Modelo para crear un estudiante

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=60)
    age = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


# Modelo para crear un tópico

class Topic(models.Model):
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=60)
    students_count = models.IntegerField(default=0, null=True, blank=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return "{} - {}".format(self.course, self.name)

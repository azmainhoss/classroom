from django.db import models
from django.urls import reverse 

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    city = models.CharField(max_length=50)
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('home')

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    student_numbers = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse ('home')

class Teacher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True) 


    def __str__(self):
        return f"{self.name} = {self.subject.name}"

    def __repr__(self):
        return f"{self.name} - {self.subject.name}"

    def get_absolute_url(self):
        return reverse ("home")        


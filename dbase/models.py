from django.db import models
from django.db.models import ManyToManyField
from django.db.models.fields import CharField, EmailField



class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_proffesor = models.CharField(max_length=100)
    course_description = models.TextField()

    
    def __str__(self):
       return self.course_name



class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_phone = models.CharField(max_length=20)



    student_enrolled_courses = models.ManyToManyField(Course, null=True, blank=True)

    def __str__(self):
            return self.student_name



#Cross-Origin Resource Sharing
#  (CORS) is a protocol that enables 
#  scripts running on a browser client
#   to interact with resources from 
#    different origin.
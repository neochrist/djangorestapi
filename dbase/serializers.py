from django.db.models import fields
from rest_framework import serializers
from .models import Student, Course

#serializers convert objects to data types
#understandable by js and front-end frameworks


class StudentSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Student
        fields = [
            'id', 'student_name', 'student_email', 
            'student_phone', 'student_enrolled_courses'
        ]

class CourseSerializer(serializers.ModelSerializer):


    class Meta:
        model = Course
        fields =[
            'id', 'course_name', 'course_proffesor',
            'course_description'
        ]

class StudentPartial(serializers.ModelSerializer):
    class Meta:
        model = Student

        fields= [
            'student_email', 'student_phone'
        ]
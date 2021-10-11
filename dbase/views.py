from functools import total_ordering
from django.db.models import query
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from typing import Type
from rest_framework.response import Response
from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer, StudentPartial
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url




schema_view = get_swagger_view(title='Inern')

urlpatterns = [
    url(r'^$', schema_view)
]

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #returns the list of students
    @extend_schema(description='<h3>/Student List</h3>')
    def list(self, request,*args, **kwargs):
        return super().list(request,*args, **kwargs)

    #creates sutdent
    @extend_schema(description='<h3>Add a Student</h3>')
    def create(sef, request,*args, **kwargs):
        return super().create(request, *args, **kwargs)

    #retrives information about student
    @extend_schema(description="<h2>Get student info.</h2>")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    #partially updates student info, 
    #needs to be changed, so 
    #only contact info will be updated

    @extend_schema(description="<h2>Partially update student info.</h2>")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    #deletes student
    @extend_schema(description="<h2>Remove student.</h2>")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

    #creates course
    @extend_schema(description='<h3>Add course.</3>')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    #returns the list of courses
    @extend_schema(description='<h2>Get list of courses.</h2>')
    def course_list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    #retrieves information about a course
    @extend_schema(description="<h2>Get course info.</h2>")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    #updates information about a course
    @extend_schema(description="<h2>Update course info.</h2>")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    #partially updates information about course
    @extend_schema(description="<h2>Partially update course info.</h2>")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    #deletes course
    @extend_schema(description="<h2>Remove course.</h2>")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


@api_view(("PUT", "DELETE"))
def add_delete(request, *args, **kwargs):

    student: Type[Student] = get_object_or_404(Student, pk=kwargs["student_id"])
    course: Type[Course] = get_object_or_404(Course, pk=kwargs["course_id"])
    if request.method == "PUT":
        student.courses.add(course)
    elif request.method == "DELETE":
        student.courses.remove(course)
        

    student.save()
    serializer = StudentSerializer(student)
    return Response(serializer.data)





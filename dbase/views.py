from functools import total_ordering
from django.db.models import query
from django.shortcuts import get_list_or_404
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer, StudentPartial
from rest_framework.parsers import JSONParser


from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse



#todo 

#assign a course to student 
#change student's only contact information

class StudentViewSet(viewsets.ModelViewSet):


    def student_list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer

        return Response(serializer.data)

class CourseViewSet(viewsets.ModelViewSet):

    def course_name(self, request):
        queryset = Course.course_name

        serializer = CourseSerializer

        return Response(serializer.data)

#todo 
# class-based-view 
# swagger 
# unit-test - prioority high 



#gets, inserts, changes or deletes
#student on a specific id
@api_view(['GET' , 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({'message': 'Student does not exist'})


    if request.method == 'GET':
        student_serializer = StudentSerializer(student)
        return JsonResponse(student_serializer.data)
    
    elif request.method == 'PUT':

        student_details = JSONParser().parse(request)

        #PATCh

        # student_detail 
        
        student_full = StudentSerializer(student, data=student_detail)
        student_serializer = StudentPartial(student, data=student_details, partial=True)

        
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(student_full.errors, status = status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'DELETED'}, status=status.HTTP_204_NO_CONTENT)



#returns student list
@api_view(['GET'])
def student_list(request):
    if request.method =='GET':
        students = Student.objects.all()

        students_serializer = StudentSerializer(students, many=True)

        return JsonResponse(students_serializer.data, safe=False)



#deletes specific course
@api_view(['GET', 'DELETE',])
def delete_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return JsonResponse({'message':'course does not exists'})
    

    if request.method == 'DELETE':
        course.delete()
        return JsonResponse({'message' : 'deleted'}, status=status.HTTP_204_NO_CONTENT)


    #returns specific course
    elif request.method == 'GET':
        course_serializer = CourseSerializer(course)
        return JsonResponse(course_serializer.data)


#adds course
@api_view(['POST'])
def add_course(request):
    if request.method == 'POST':

        course_data = JSONParser().parse(request)
        course_serializer = CourseSerializer(data=course_data)

        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse(course_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(course_serializer.errors, status=status.HTTP_404_NOT_FOUND)







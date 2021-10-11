from django.conf.urls import url
from rest_framework import urlpatterns
from .views import StudentViewSet, CourseViewSet, add_delete
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()

router.register("student", StudentViewSet, basename="student")
router.register("course", CourseViewSet, basename="course")

urlpatterns = [
    path('', include(router.urls)),
    path('student/<int:student_id>/int:course_di>/', add_delete, name="add_delete")
    
]
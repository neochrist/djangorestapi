from django.conf.urls import url
from rest_framework import urlpatterns
from .views import StudentViewSet, CourseViewSet, add_delete
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='TEST API')


router = DefaultRouter()

router.register("student", StudentViewSet, basename="student")
router.register("course", CourseViewSet, basename="course")

urlpatterns = [
    url(r'^$', schema_view),
    path('', include(router.urls)),
    path('student/<int:student_id>/int:course_di>/', add_delete, name="add_delete")
]
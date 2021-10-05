from django.conf.urls import url
from rest_framework import urlpatterns

from dbase import views

urlpatterns = [
    url(r'^api/dbase/students$' , views.student_list),
    url(r'^api/dbase/students(?P<pk>[0-9]+)$', views.student_detail),
    url(r'^api/dbase/courses$', views.add_course),
    url(r'^api/dbase/courses(?P<pk>[0-9]+)$', views.delete_course)
    
]
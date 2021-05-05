
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'quiz'

urlpatterns = [

    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^quiz_world/$', views.quiz_world, name='quiz_world'),
    path('quiz_world/<course_name>/', views.quizview),

]

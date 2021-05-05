from django.contrib import admin
from quiz.models import UserProfileInfo, User
from quiz.models import Question
from quiz.models import Course
# from quiz.models import Quizheading

# Register your models here.

admin.site.register(UserProfileInfo)
# admin.site.register(Choice)
# admin.site.register(Quizheading)
admin.site.register(Course)
admin.site.register(Question)

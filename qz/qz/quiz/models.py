# quiz/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
   course_name = models.CharField(max_length=50)
   date_added = models.DateField(default=timezone.now())
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()

   def __str__(self):
        return self.course_name


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.CharField(max_length=200)
    marks = models.PositiveIntegerField()
    Add_only_Textfield = models.BooleanField(default=False)
    choice1 = models.CharField(max_length=50, unique=True)
    choice2 = models.CharField(max_length=50, unique=True)
    choice3 = models.CharField(max_length=50, unique=True, blank=True)
    choice4 = models.CharField(max_length=50, unique=True, blank=True)
    cat = (('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'))
    answer = models.CharField(max_length=200, choices=cat)

    def __str__(self):
        return self.questions

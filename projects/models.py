from django.db import models

# Create your models here.
import datetime
import os
from django.core.validators import MinValueValidator, MaxValueValidator

class ContactUs (models.Model):
    first_name_contact_us = models.CharField(max_length=120)
    last_name_contact_us = models.CharField(max_length=120)
    email_contact_us = models.EmailField()
    number_contact_us = models.IntegerField()
    inquiry_contact_us = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.first_name_contact_us} {self.last_name_contact_us} email {self.email_contact_us}.'
    
    
class TrackTeacherModel(models.Model):
    oldfile = models.FileField(upload_to='track_teachers/' )
    newfile = models.FileField(upload_to='track_teachers/')

    def __str__(self):
        return f'first is   {self.oldfile} and second  is  {self.newfile}'

topic_language = (('English', 'english'), 
                  ('Arabic', 'arabic'))

class ExamGPTModel(models.Model):
    lesson_name = models.CharField(max_length=300)
    subject = models.CharField(max_length=50)
    grade = models.CharField(max_length=12)
    school_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=60)
    topic_language =  models.CharField(choices=topic_language ,max_length=100)
    def __str__(self):
        return f'A teacher {self.teacher_name} created a Quiz about {self.lesson_name}'

class LessonPlanGPTModel(models.Model):
    lesson_name = models.CharField(max_length=500)
    subject = models.CharField(max_length=50)
    grade = models.CharField(max_length=12)
    school_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=60)
    def __str__(self):
        return f'A teacher {self.teacher_name} created a lesson plan about {self.lesson_name}'
    
    
    
class Donate(models.Model):
    full_name = models.CharField(max_length=120, default='unknown')
    email = models.EmailField(default='unknown mail')
    amount = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.full_name} donated {self.amount}."
    
    
class ExamGPTWhisperModel(models.Model):
    lesson_name = models.CharField(max_length=500)
    def __str__(self):
        return f'A teacher created a Quiz about {self.lesson_name}'
    
class LessonGPTWhisperModel(models.Model):
    lesson_name = models.CharField(max_length=500)
    def __str__(self):
        return f'A teacher created a lesson plan about {self.lesson_name}'
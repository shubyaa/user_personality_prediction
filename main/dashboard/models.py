import email
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=2)
    description = models.TextField()
    email = models.EmailField(default='')
    phone = models.CharField(default=0, max_length=12)
    area = models.CharField(default='Mumbai', max_length=50)
    state = models.CharField(default='Maharashtra', max_length=50)
    country_code = models.CharField(default='IN', max_length=5)
    

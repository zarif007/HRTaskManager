from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class Task(models.Model):

    assign_status_options = (
        (0, 'Unasigned'),
        (1, 'Assigned'),
    )

    status_options = (
        (0, 'On going'),
        (1, 'Done'),
    )

    task_name = models.CharField(max_length=100)
    assign_date =  models.DateField(default=datetime.now, blank=True)
    last_date = models.DateField(default=datetime.now, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=100, null=True)
    status = models.BooleanField(choices=status_options, null=True)
    assign_status = models.BooleanField(choices=assign_status_options, null=True, default=0)
    code = models.CharField(max_length=8, unique=True, null=True)
    member = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.task_name

class User(AbstractUser):

    designation_options = (
        ('General Member', 'General Member'),
        ('Executive', 'Executive'),
        ('Senior Executive', 'Senior Executive'),
        ('Assistant Director', 'Assistant Director'),
        ('Director', 'Director'),
    )

    department_options = (
        ('HR', 'Human Resources'),
    )

    status_options = (
        (0, 'Free'),
        (1, 'Busy'),
    )   

    password2 = models.CharField(max_length=150, null=True)
    in_club_name = models.CharField(max_length=70, blank=True)
    department = models.CharField(max_length=50, choices=department_options, blank=True)
    designation = models.CharField(max_length=20, choices=designation_options, blank=True)
    display_picture = models.ImageField(blank=True, null=True)
    status = models.BooleanField(choices=status_options, default=1, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    hr_points = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.username + '( ' + self.in_club_name + ')'



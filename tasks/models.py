from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class Task(models.Model):

    assingn_status_options = (
        (0, 'Unasigned'),
        (1, 'Assigned'),
    )

    status_options = (
        (0, 'On going'),
        (1, 'Done'),
    )

    task_name = models.CharField(max_length=100, blank=True)
    assign_date =  models.DateField(default=datetime.now, blank=True)
    last_date = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=200, blank=True)
    url = models.URLField(max_length=100, null=True)
    status = models.BooleanField(choices=status_options, null=True)
    assign_status = models.BooleanField(choices=assingn_status_options, null=True)
    member = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.task_name

class User(AbstractUser):

    designation_options = (
        ('draft', 'Draft'),
        ('publishd', 'Published'),
    )

    department_options = (
        ('draft', 'Draft'),
        ('publishd', 'Published'),
    )

    status_options = (
        (0, 'Free'),
        (1, 'Busy'),
    )

    name = models.CharField(max_length=50)
    in_club_name = models.CharField(max_length=70)
    department = models.CharField(max_length=50, choices=department_options)
    designation = models.CharField(max_length=20, choices=designation_options)
    display_picture = models.ImageField(blank=True, null=True)
    status = models.BooleanField(choices=status_options, default=1)

    def __str__(self):
        return self.name
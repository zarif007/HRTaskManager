from django.contrib import admin
from .models import User, Task, Event

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Event)
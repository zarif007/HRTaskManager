from django.contrib import admin
from .models import User, Task, Event, Announcements

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Event)
admin.site.register(Announcements)

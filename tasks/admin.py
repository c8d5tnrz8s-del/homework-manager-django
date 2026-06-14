from django.contrib import admin
from .models import Homework, Subject, Student

admin.site.register(Homework)
admin.site.register(Subject)
admin.site.register(Student)
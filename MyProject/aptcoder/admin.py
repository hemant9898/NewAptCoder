from django.contrib import admin

# Register your models here.

from .models import Teacher, Student, Course

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
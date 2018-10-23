from django.contrib import admin
from inspire.models import Course, CourseInstance, Professor, Student

admin.site.register(Course)
admin.site.register(CourseInstance)
admin.site.register(Professor)
admin.site.register(Student)

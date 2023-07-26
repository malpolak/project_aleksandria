from django.contrib import admin
from .models import Course, Enrollment, Review

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'start_date', 'end_date']

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment)
admin.site.register(Review)

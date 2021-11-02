from django.contrib import admin
from .models import Student, Topic


class StudentAdmin(admin.ModelAdmin):
    model = Student
    fields = ['name', 'surname', 'age']
    list_display = ['id', 'name', 'surname', 'age']
    list_filter = ['age']


class TopicAdmin(admin.ModelAdmin):
    model = Topic


admin.site.register(Student, StudentAdmin)
admin.site.register(Topic, TopicAdmin)


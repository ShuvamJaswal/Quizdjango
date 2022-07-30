from django.contrib import admin
from .models import *
from quiz_app_teacher.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Course)
admin.site.register(Result)

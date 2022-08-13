# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User, Student, Teacher


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
        'first_name',
        'email',
        'is_student',
        'is_teacher',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'is_student',
        'is_teacher',
    )
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    list_filter = ('course',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',)

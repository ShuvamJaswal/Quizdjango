# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User, Student, Teacher


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'date_joined',
        'is_student',
        'is_teacher',
        'password',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'date_joined',
        'is_student',
        'is_teacher',
    )
    raw_id_fields = ('groups', 'user_permissions')
    search_fields = ('username',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    list_filter = ('course',)
    search_fields = ('user__username',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

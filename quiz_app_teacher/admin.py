# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Course, Quiz, Result, Question


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')
    search_fields = ('name',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'quiz_id',
        'created_date',
        'author',
        'course',
    )
    list_filter = ('created_date', 'author', 'course')
    search_fields = ('name',)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'quiz',
        'points',
        'answer_data',
        'max_points',
        'submitted_at',
    )
    list_filter = ('student', 'quiz', 'submitted_at')
    


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'quiz',
        'question',
        'A',
        'B',
        'C',
        'D',
        'answer',
        'question_number',
    )
    list_filter = ('quiz',)
    search_fields = ('question',)

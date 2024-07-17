from django.contrib import admin
from .models import  Darslar, Kurslar, Izohlar, User,LikeText



@admin.register(Kurslar)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'kursi']
    list_editable = ['kursi']
    list_display_links = ['pk']


@admin.register(Darslar)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'kursi', 'dars', 'izohi', 'muallifi','video']
    list_editable = ['izohi']
    list_display_links = ['pk', 'dars']


@admin.register(Izohlar)
class LessonCommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'darsi', 'muallifi', 'izohi']
    list_editable = ['izohi']
    list_display_links = ['pk', 'darsi']

@admin.register(LikeText)
class LikeLessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dars_like', 'like_or_dislike', 'author', 'created']
    list_display_links = ['pk', 'author']


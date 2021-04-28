from django.contrib import admin
from django import forms
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # form = CoursesAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'description', 'price', 'photo',
                    'get_photo', 'methods', 'questions', 'teachers', 'students')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', )
    readonly_fields = ('get_photo',)
    fields = ('title', 'slug', 'category', 'description', 'price', 'photo', 'get_photo', 'methods', 'teachers',
              'questions', 'students')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # form = CoursesAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'slug', 'age', 'phone', 'email', 'experience', 'photo', 'get_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('experience', )
    readonly_fields = ('get_photo',)
    fields = ('name', 'slug', 'age', 'phone', 'email', 'experience', 'photo', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # form = CoursesAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'slug', 'age', 'phone', 'email', 'rating', 'photo', 'get_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('rating', )
    readonly_fields = ('get_photo',)
    fields = ('name', 'slug', 'age', 'phone', 'email', 'rating', 'photo', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # form = CoursesAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    fields = ('title', 'slug')

# -*- coding: UTF-8 -*-

from django.contrib import admin
from core import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class TourAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'description', 'comment', 'price')


class ExtendedTourAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'description', 'comment', 'price')


class PersonRequestAdmin(admin.ModelAdmin):
    list_display = ('state', 'date', 'message', 'name', 'email', 'phone_number')


class SliderItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'category')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.ExtendedTour, ExtendedTourAdmin)
admin.site.register(models.PersonRequest, PersonRequestAdmin)
admin.site.register(models.SliderItem, SliderItemAdmin)
admin.site.register(models.Article, ArticleAdmin)

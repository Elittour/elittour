# coding=utf-8
from django.template.defaulttags import register
from core.models import Category

@register.filter
def get_url_for_category_name(category):
    return Category.objects.get(name=category[0].name).url

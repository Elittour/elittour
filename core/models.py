# -*- coding: UTF-8 -*-

import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название категории')
    description = models.TextField(verbose_name=u'Описание категории', null=True, blank=True)
    url = models.CharField(verbose_name=u'Ссылка до страницы с категорией', max_length=255)

    class Meta:
        verbose_name = u'категорию'
        verbose_name_plural = u'категории'

    def __unicode__(self):
        return self.name

class PersonRequest(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата заявки', auto_now_add=True)
    name = models.CharField(verbose_name=u'Имя', max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name=u"Электронная почта")
    phone_number = models.IntegerField(verbose_name=u'Телефонный номер', blank=True, null=True)
    message = models.TextField(verbose_name=u'Сообщение')
    state = models.BooleanField(verbose_name=u'Рассмотрен', default=False)

    def __unicode__(self):
        return u'%s[%s]' % (self.name, self.message)

    @property
    def mail(self):
        return u'Дата заявки: %s; ' \
               u'Имя: %s; ' \
               u'Электронная почта: %s; ' \
               u'Телефонный номер: %s; ' \
               u'Сообщение: %s; ' % (self.date, self.name, self.email, self.phone_number, self.message)

    class Meta:
        verbose_name = u"заявку"
        verbose_name_plural = u"заявки"


class SliderItem(models.Model):
    title = models.TextField(verbose_name=u'Заголовок')
    title_color = models.CharField(max_length=100, verbose_name=u'Цвет заголовка', default='black')
    text = models.TextField(verbose_name=u'Текст')
    text_color = models.CharField(max_length=100, verbose_name=u'Цвет текста', default='black')
    category = models.ForeignKey(Category, verbose_name=u'Категория', blank=True, null=True,
                                 help_text=u'Будет создавать сылку на страницу с категорией')
    img = models.ImageField(upload_to='slider/', verbose_name=u'Изображение')
    active = models.BooleanField(verbose_name=u'Показывать', default=False)
    desc_color = models.CharField(max_length=100, verbose_name=u'Цвет "Подробнее"', default='black')

    substrate_color = models.CharField(max_length=100, verbose_name=u'Цвет подложки', default='white',
                                       help_text=u'если нужна прозрачность то пишите RGB цвет => rgba(0, 0, 0, 1),'
                                                 u' где 4 атрибут это прозрачность')

    def delete(self, using=None):
        """ Логика удаления картинки тура """
        os.remove(self.img.path)
        super(SliderItem, self).delete(using=using)

    class Meta:
        verbose_name = u"слайд"
        verbose_name_plural = u"слайды"


@receiver(pre_delete, sender=SliderItem)
def img_delete_signal(sender, **kwargs):
    """ Удаление изображения слайдера , если удаляли пачками """
    os.remove(kwargs['instance'].img.path)


class Tour(models.Model):
    name = models.TextField(verbose_name=u'Название')
    color_name = models.CharField(max_length=100, verbose_name=u'Цвет заголовка', default='black')
    date = models.DateField(max_length=100, verbose_name=u'Дата')
    color_date = models.CharField(max_length=100, verbose_name=u'Цвет даты', default='black')
    category = models.ManyToManyField(Category, verbose_name=u'Категория')
    description = models.TextField(verbose_name=u"Описание")
    price = models.IntegerField(verbose_name=u'Цена (в рублях)')
    color_price = models.CharField(max_length=100, verbose_name=u'Цвет цены', default='black')
    comment = models.TextField(verbose_name=u'Комментарий', null=True, blank=True)
    img = models.ImageField(upload_to='image-tour/', verbose_name=u'Изображение', null=True, blank=True)
    active = models.BooleanField(verbose_name=u'Выдавать на страницу', default=False)
    active_for_right = models.BooleanField(verbose_name=u'Выдавать в правом блоке', default=False)

    # TODO TODO TODO убрать эту дичь
    number = models.IntegerField(verbose_name=u'Код', help_text=u'Для фильтрации , формируется из даты')

    def delete(self, using=None):
        """ Логика удаления картинки тура """
        if self.img:
            os.remove(self.img.path)
        super(Tour, self).delete(using=using)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u"автобусный тур"
        verbose_name_plural = u"автобусные туры"


class ExtendedTour(Tour):
    class Meta:
        verbose_name = u"тур"
        verbose_name_plural = u"туры"


class Article(models.Model):
    name = models.TextField(verbose_name=u'Название')
    category = models.ManyToManyField(Category, verbose_name=u'Категория')
    article = models.TextField(verbose_name=u'Статья')
    show = models.BooleanField(verbose_name=u'Показать', default=False)

    img = models.ImageField(upload_to='image-tour/', verbose_name=u'Изображение', null=True, blank=True)
    active_for_right = models.BooleanField(verbose_name=u'Выдавать в правом блоке', default=False)

    # TODO TODO TODO убрать эту дичь
    number = models.IntegerField(verbose_name=u'Код', help_text=u'Для фильтрации , формируется из даты')

    def delete(self, using=None):
        """ Логика удаления картинки тура """
        if self.img:
            os.remove(self.img.path)
        super(Article, self).delete(using=using)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u"стаью"
        verbose_name_plural = u"статьи"


@receiver(pre_delete, sender=Article)
def img_delete_signal(sender, **kwargs):
    """ Удаление изображения статьи , если удаляли пачками """
    if kwargs['instance'].img:
        os.remove(kwargs['instance'].img.path)


@receiver(pre_delete, sender=Tour)
def img_delete_signal(sender, **kwargs):
    """ Удаление изображения тура , если удаляли пачками """
    if kwargs['instance'].img:
        os.remove(kwargs['instance'].img.path)
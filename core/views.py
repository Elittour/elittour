# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from core import models, forms
from django.core.mail import send_mail


class BasePage(TemplateView):
    template_name = 'elittour/base.html'
    title = None
    category_name = None
    category = None

    def get_context_data(self, **kwargs):
        c = {
            u'feedback_form': forms.FeedbackForm(),
            u'sliders': models.SliderItem.objects.all(),
            u'title': self.title,
            u'tours': models.Tour.objects.filter(active_for_right=True).order_by('number'),
            u'articles': models.Article.objects.filter(active_for_right=True).order_by('number')
        }
        try:
            self.category = models.Category.objects.get(name=self.category_name)
            article = models.Article.objects.filter(category=self.category, show=True)[0]
            c[u'article'] = article
            print self.category
        finally:
            return c


class Index(BasePage):
    title = 'Элит-Тур'
index = Index.as_view()


class Index1(BasePage):
    title = 'Элит-Тур'
    template_name = 'elittour/base1.html'
index1 = Index1.as_view()

class Railway(BasePage):
    title = 'Продажа ж\д и авиа билетов'
railway = Railway.as_view()


class Passport(BasePage):
    title = 'Загранпаспорт и визы'
passport = Passport.as_view()


class Contacts(BasePage):
    title = 'Контакты'
contacts = Contacts.as_view()


class Months(BasePage):
    template_name = 'elittour/months/general_month.html'

    def get_context_data(self, **kwargs):
        c = super(Months, self).get_context_data(**kwargs)
        if self.category:
            tours = models.Tour.objects.filter(category=self.category)
            c[u'tours'] = tours
            c[u'title'] = self.category_name
            c[u'description'] = self.category.description

        return c


class Ded(BasePage):
    template_name = 'elittour/months/ded.html'

    def get_context_data(self, **kwargs):
        c = super(Ded, self).get_context_data(**kwargs)
        if self.category:
            tours = models.Tour.objects.filter(category=self.category)
            c[u'tours'] = tours
            c[u'description'] = self.category.description
        return c


class Country(BasePage):
    tmp = None
    category_name = None

    @property
    def template_name(self):
        return 'elittour/country/%s.html' % self.tmp


class SearchTour(BasePage):
    template_name = 'elittour/poisk-tura.html'
search_tour = SearchTour.as_view()


class Moscow(BasePage):
    category_name = u'Туры в Москву'
    template_name = 'elittour/tury-v-moskvu.html'
    model = models.Tour

    def get_context_data(self, **kwargs):
        c = super(Moscow, self).get_context_data(**kwargs)
        try:
            category = models.Category.objects.get(name=self.category_name)
            tours = self.model.objects.filter(category=category)
        except models.Category.DoesNotExist:
            tours = None
        c[u'tours'] = tours
        return c
moscow = Moscow.as_view()

class Koncert(BasePage):
    category_name = u'Концерты'
    template_name = 'elittour/koncert.html'
    model = models.Tour

    def get_context_data(self, **kwargs):
        c = super(Koncert, self).get_context_data(**kwargs)
        try:
            category = models.Category.objects.get(name=self.category_name)
            tours = self.model.objects.filter(category=category)
        except models.Category.DoesNotExist:
            tours = None
        c[u'tours'] = tours
        return c
koncert = Koncert.as_view()

class Gorjashhie(BasePage):
    category_name = u'Горящие туры'
    template_name = 'elittour/koncert.html'
    model = models.Tour

    def get_context_data(self, **kwargs):
        c = super(Gorjashhie, self).get_context_data(**kwargs)
        try:
            category = models.Category.objects.get(name=self.category_name)
            tours = self.model.objects.filter(category=category)
        except models.Category.DoesNotExist:
            tours = None
        c[u'tours'] = tours
        return c
gorjashhie = Gorjashhie.as_view()



class Ex(Moscow):
    category_name = u'Экзотика'
    template_name = 'elittour/jekzoticheskie-tury.html'
    model = models.ExtendedTour
ekzotika = Ex.as_view()



def create_person_request(request):
    """ Ajax """
    c = {}
    form = forms.FeedbackForm(request.POST or None)
    if form.is_valid():
        # print form.cleaned_data
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        phone_number = form.cleaned_data.get('phone_number')
        message = form.cleaned_data.get('message')
        models.PersonRequest.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message,
        )
        subject = u'Зыявка на экскурсию'
        message = u'телефон: %s \n Имя: %s \n Email: %s \n Сообщение: %s' % (phone_number, name, email, message)
        send_mail(subject, message, 'workmailer2016@gmail.com', [ 'elitserp@yandex.ru', 'oli5vka@gmail.com'], fail_silently=False)
        return HttpResponse('Ok')
    c['feedback_form'] = form
    return render(request, 'elittour/items/feedbackform.html', c)


def zagranpasport(request):
    c = dict(feedback_form=forms.FeedbackForm(), sliders=models.SliderItem.objects.all(),
             title='Оформление загранпаспорта', tours=models.Tour.objects.filter(active_for_right=True),
             articles=models.Article.objects.filter(active_for_right=True))
    return render(request, 'elittour/zagranpasport.html', c)

#   function name
def viza(request):
    c = dict(feedback_form=forms.FeedbackForm(), sliders=models.SliderItem.objects.all(),
             title='Оформление визы', tours=models.Tour.objects.filter(active_for_right=True),
             articles=models.Article.objects.filter(active_for_right=True))
    return render(request, 'elittour/viza.html', c)

def bilet(request):
    c = dict(feedback_form=forms.FeedbackForm(), sliders=models.SliderItem.objects.all(),
             title='Продажа авиа и железнодорожных билетов', tours=models.Tour.objects.filter(active_for_right=True),
             articles=models.Article.objects.filter(active_for_right=True))
    return render(request, 'elittour/bilet.html', c)

def transfer(request):
    c = dict(feedback_form=forms.FeedbackForm(), sliders=models.SliderItem.objects.all(),
             title='Трансфер в аэропорт и на железнодорожный вокзал', tours=models.Tour.objects.filter(active_for_right=True),
             articles=models.Article.objects.filter(active_for_right=True))
    return render(request, 'elittour/transfer.html', c)

def avia(request):
    c = dict(feedback_form=forms.FeedbackForm(), sliders=models.SliderItem.objects.all(),
             title='Регистрация на рейс', tours=models.Tour.objects.filter(active_for_right=True),
             articles=models.Article.objects.filter(active_for_right=True))
    return render(request, 'elittour/avia.html', c)

def strashovka(request):
    c = dict(feedback_form=forms.FeedbackForm(), sliders=models.SliderItem.objects.all(),
             title='Туристическое страхование', tours=models.Tour.objects.filter(active_for_right=True),
             articles=models.Article.objects.filter(active_for_right=True))
    return render(request, 'elittour/strashovka.html', c)

def kredit(request):
    c = dict(feedback_form=forms.FeedbackForm(), sliders=models.SliderItem.objects.all(),
             title='Продажа туров в кредит', tours=models.Tour.objects.filter(active_for_right=True),
             articles=models.Article.objects.filter(active_for_right=True))
    return render(request, 'elittour/kredit.html', c)

def sandom(request):
    c = dict(feedback_form=forms.FeedbackForm(), sliders=models.SliderItem.objects.all(),
             title='Санаторий на дому', tours=models.Tour.objects.filter(active_for_right=True),
             articles=models.Article.objects.filter(active_for_right=True))
    return render(request, 'elittour/sandom.html', c)


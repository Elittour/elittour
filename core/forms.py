# coding=utf-8
from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label=u'Имя', max_length=255)
    email = forms.EmailField(label=u'Почта', max_length=255)
    phone_number = forms.IntegerField(label=u'Номер телефона')
    message = forms.CharField(label=u'Заявка', help_text=u'(место, цена, условия)', widget=forms.Textarea)

    def clean_phone_number(self):
        number = self.cleaned_data['phone_number']
        # TODO написать валидаци по полю номера
        return number


class CallBackForm(forms.Form):
    number = forms.CharField(label=u'Ваш номер')
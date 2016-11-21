# -*- coding: UTF-8 -*-
from core.views import index, contacts, passport, Months, Country, search_tour, moscow, ekzotika, sandom, \
    create_person_request, Ded, zagranpasport, viza, bilet, transfer, avia, strashovka, kredit, gorjashhie
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from core import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='elittour'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create_person_request/$', create_person_request, name='create_person_request'),
# туры по типам
    url(r'^tury-v-moskvu/$', moscow, name='moscow'),
    url(r'^jekzoticheskie-tury/$', ekzotika, name='ekzotika'),
    url(r'^gorjashhie-tury/$',gorjashhie, name='gorjashhie'),


# туры по месяцам
    url(r"^tury-po-mesjacam/tury-v-janvare/$", Months.as_view(category_name=u'Туры в Январе'), name='january'),
    url(r"^tury-po-mesjacam/tury-v-fevrale/$", Months.as_view(category_name=u'Туры в Феврале'), name='february'),
    url(r"^tury-po-mesjacam/tury-v-marte/$", Months.as_view(category_name=u'Туры в Марте'), name='march'),
    url(r"^tury-po-mesjacam/tury-v-aprele/$", Months.as_view(category_name=u'Туры в Апреле'), name='april'),
    url(r"^tury-po-mesjacam/tury-v-mae/$", Months.as_view(category_name=u'Туры в Мае'), name='may'),
    url(r"^tury-po-mesjacam/tury-v-ijune/$", Months.as_view(category_name=u'Туры в Июне'), name='june'),
    url(r"^tury-po-mesjacam/tury-v-ijule/$", Months.as_view(category_name=u'Туры в Июле'), name='july'),
    url(r"^tury-po-mesjacam/tury-v-avguste/$", Months.as_view(category_name=u'Туры в Августе'), name='august'),
    url(r"^tury-po-mesjacam/tury-v-sentjabre/$", Months.as_view(category_name=u'Туры в Сентябре'), name='september'),
    url(r"^tury-po-mesjacam/tury-v-oktjabre/$", Months.as_view(category_name=u'Туры в Октябре'), name='october'),
    url(r"^tury-po-mesjacam/tury-v-nojabre/$", Months.as_view(category_name=u'Туры в Ноябре'), name='november'),
    url(r"^tury-po-mesjacam/tury-v-dekabre/$", Months.as_view(category_name=u'Туры в Декабре'), name='december'),
# туры по странам
    url(r"^tury-po-stranam/tury-po-italii/$",
        Country.as_view(tmp='tury-po-italii', category_name=u'Туры по Италии'), name='italy'),
    url(r"^tury-po-stranam/tury-vo-franciju/$",
        Country.as_view(tmp='tury-vo-franciju', category_name=u'Туры во Францию'), name='francija'),
    url(r"^tury-po-stranam/tury-v-greciju/$",
        Country.as_view(tmp='tury-v-greciju', category_name=u'Туры в Грецию'), name='grecija'),
    url(r"^tury-po-stranam/tury-po-turcii/$",
        Country.as_view(tmp='tury-po-turcii', category_name=u'Туры по Турции'), name='turkey'),
    url(r"^tury-po-stranam/tury-v-egipet/$",
        Country.as_view(tmp='tury-v-egipet', category_name=u'Туры в Египет'), name='egipet'),
    url(r"^tury-po-stranam/tury-po-ispanii/$",
        Country.as_view(tmp='tury-po-ispanii', category_name=u'Туры по Испании'), name='spain'),
    url(r"^tury-po-stranam/tury-v-portugaliju/$",
        Country.as_view(tmp='tury-v-portugaliju', category_name=u'Туры в Португалию'), name='portugalija'),
    url(r"^tury-po-stranam/tury-v-izrailju/$",
        Country.as_view(tmp='tury-po-izrailju', category_name=u'Туры по Израилю'), name='israel'),
    url(r"^tury-po-stranam/tury-v-vengriju/$",
        Country.as_view(tmp='tury-v-vengriju', category_name=u'Туры в Венгрию'), name='vengrija'),
    url(r"^tury-po-stranam/tury-v-indiju/$",
        Country.as_view(tmp='tury-v-indiju', category_name=u'Туры в Индию'), name='indija'),
    url(r"^tury-po-stranam/tury-na-kipr/$",
        Country.as_view(tmp='tury-na-kipr', category_name=u'Туры на Кипр'), name='kipr'),
    url(r"^tury-po-stranam/tury-v-norvegiju/$",
        Country.as_view(tmp='tury-v-norvegiju', category_name=u'Туры в Норвегию'), name='norvegija'),
    url(r"^tury-po-stranam/tury-v-finljandiju/$",
        Country.as_view(tmp='tury-v-finljandiju', category_name=u'Туры в Финляндию'), name='finljandija'),
     url(r"^tury-po-stranam/tury-v-tailand/$",
        Country.as_view(tmp='tury-v-tailand', category_name=u'Туры в Таиланд'), name='tailand'),

# туры по типам
    url(r"^tury-po-rossii/$",
        Country.as_view(tmp='russia', category_name=u'Туры по России'), name='russia'),
    url(r"^tury-v-belarus/$",
        Country.as_view(tmp='tury-v-belarus', category_name=u'Туры в Беларусь'), name='belarus'),

    url(r"^jekskursionnye-tury/$",
        Country.as_view(tmp='jekskursionnye-tury', category_name=u'Туры по Европе'), name='europe'),
    url(r"^gorjashhie-tury/$",
        Country.as_view(tmp='gorjashhie-tury', category_name=u'Горящие туры'), name='gorjashhie'),
     url(r"^tury-po-stranam/avtobusnye-tury-v-evropu/$",
        Country.as_view(tmp='avtobusnye-tury-v-evropu', category_name=u'Автобусные туры в Европу'), name='bus-evropa'),
    url(r"^tury-po-stranam/jekskursionnye-tury-v-evropu/$",
        Country.as_view(tmp='jekskursionnye-tury-v-evropu', category_name=u'Экскурсионные туры в Европу'), name='eks-evropa'),
    url(r"^tury-po-stranam/avtobusom-k-morju/$",
        Country.as_view(tmp='avtobusom-k-morju', category_name=u'Автобусом к морю'), name='avtobusomkmorju'),





    url(r"^velikij-ustjug/$", Ded.as_view(category_name=u'Великий Устюг'), name='ded'),

    url(r"^poisk-tura/$", search_tour, name='search_tour'),

# услуги
    url(r"^oformlenie-zagranpasporta/$", zagranpasport, name='zagranpasport'),
    url(r"^oformlenie-vizi/$", viza, name='viza'),
    url(r"^prodazha-aviabiletov/$", bilet, name='bilet'),
    url(r"^transfer-v-ajeroport/$", transfer, name='transfer'),
    url(r"^registracija-na-aviarejs/$", avia, name='avia'),
    url(r"^turisticheskoe-strahovanie/$", strashovka, name='strashovka'),
    url(r"^otdyh-v-kredit/$", kredit, name='kredit'),
    url(r"^sanatorij-na-domu/$", sandom, name='sandom'),
       #   path in url        function   in menu
)

if not settings.DEBUG:
    urlpatterns += patterns("django.views",
                            url(r"%s(?P<path>.*)$" % settings.STATIC_URL[1:], "static.serve", {
                                "document_root": settings.STATIC_ROOT, 'show_indexes': True, }, name='static_image'),
                            )
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
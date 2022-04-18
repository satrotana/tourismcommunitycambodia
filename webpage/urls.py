
from django.urls import path
from webpage import views

# app_name = 'webpage'
urlpatterns = [
    path('', views.home, name='home'),
    path('nactec_national', views.about_nactec_national, name='nactec_national'),
    path('about_nactec_city_town', views.about_nactec_city_town, name='about_nactec_city_town'),
    path('documentations', views.documentations, name='documentations'),
    path('documentations_other', views.documentations_other, name='documentations_other'),
    path('news', views.news, name='news'),
    path('news/<int:id>', views.news_details, name='news/<int:id>'),
    path('community', views.community, name='community'),
    path('contact', views.contact, name='contact'),
]

from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^education/', views.education, name='education'),
    url(r'^training/', views.training, name='training'),
    url(r'^employment/', views.employment, name='employment'),
    url(r'^portfolio/', views.portfolio, name='portfolio'),
    url(r'^contact/', views.contact, name='contact'),
    #url(r'Contact/', views.Contact, name='Contact'),

]

#https://www.christiaan.com/thoughts/django-email-form-and-smtp-settings-tutorial/
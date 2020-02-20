from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
    path('book', views.book, name='book'),
    path('contact_confirm', views.contact_confirm, name='contact_confirm'),
    path('book_confirm', views.book_confirm, name='book_confirm'),
    path('oops', views.oops, name='oops')
]

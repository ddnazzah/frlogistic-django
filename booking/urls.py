from django.urls import path
from django.conf.urls import url, handler404
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('success', views.email_success, name='success'),
    path('terms', views.terms, name='terms'),
    path('book', views.book, name='book'),
    path('contact_confirm', views.contact_confirm, name='contact_confirm'),
    path('book_confirm', views.book_confirm, name='book_confirm'),
    path('export/deliveries', views.export_delivery_data_csv, name='export_delivery_data'),
    path('export/safekeeping_data', views.export_safekeeping_data_csv, name='export_safekeeping_data'),
    path('export/warehouse_date', views.export_warehousing_data_csv, name='export_warehouse_data'),
    path("robots.txt",TemplateView.as_view(template_name="booking/robots.txt", content_type="text/plain"),),
]





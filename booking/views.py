import csv
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .forms import *
from .models import *

now = datetime.datetime.today()
date = now.date()

def index(request):
    return render(request, 'booking/index.html', {'title': 'FR Logistics - Your Fast and Reliable logistics solution', 'description': 'A Ghanaian based logistics company that is intent on offering Fast and Reliable services such as door to door delivery of logistics, safekeeping of items for students and warehousing solutions'})


def about(request):
    return render(request, 'booking/about.html', {'title': 'About - FR Logistics', 'description': 'All you need to know about FR logistics; your best delivery service in Ghana'})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = f"Name : {form.cleaned_data['name']}  \nEmail : {form.cleaned_data['email']} \nMessage : {form.cleaned_data['message']}"
            try:
                send_mail(name, message, email, ['frlogistics0@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('contact_confirm')

    return render(request, 'booking/contact.html', {'title': 'Contact - FR Logistics', 'form': form})


def email_success(request):
    return render(request, 'booking/success.html', {'title': 'Contact - FR Logistics', 'description': 'Reach Fast, Reliable logistics here'})


def terms(request):
    return render(request, 'booking/terms.html', {'title': 'Terms and Conditions - FR Logistics'})


def book(request):
    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        safekeeping_form = SafeKeepingForm(request.POST)
        warehousing_form = WarehousingForm(request.POST)

        if delivery_form.is_valid():
            delivery_form.save()
            return redirect('book_confirm')

        if safekeeping_form.is_valid():
            safekeeping_form.save()
            return redirect('book_confirm')

        if warehousing_form.is_valid():
            warehousing_form.save()
            return redirect('book_confirm')

    else:
        delivery_form = DeliveryForm()
        safekeeping_form = SafeKeepingForm()
        warehousing_form = WarehousingForm()

    context = {
        'title': 'Book Our Services - FR Logistics',
        'delivery_form': delivery_form,
        'safekeeping_form': safekeeping_form,
        'warehousing_form': warehousing_form,
        'description': 'Book for delivery services across Ghana, warehousing solutions for logistics and safekeeping of items for students',
    }
    return render(request, 'booking/book.html', context)


def contact_confirm(request):
    context = {'title': 'Success - FR Logistics'}
    return render(request, 'booking/contact_confirm.html', context)


def book_confirm(request):
    context = {'title': 'Success - FR Logistics'}
    return render(request, 'booking/book_confirm.html', context)

def export_delivery_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="delivery.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Contact', 'Location From', 'Location To', 'Items List'])
    deliveries = DeliveryModel.objects.filter(currentdate=date).values_list('name', 'email', 'contact', 'location_from', 'location_to',
                                                         'items_list')
    for delivery in deliveries:
        writer.writerow(delivery)
    return response


def export_safekeeping_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="safekeeping.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Contact', 'Location From', 'Date', 'Items List'])
    safekeeping_items = SafeKeepingModel.objects.filter(currentdate=date).values_list('name', 'email', 'contact', 'location_from', 'date',
                                                                   'items_list')
    for safekeeping_item in safekeeping_items:
        writer.writerow(safekeeping_item)
    return response


def export_warehousing_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="warehouse.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Name of Business', 'Email', 'Contact', 'Location From', 'Items List'])
    warehouse_items = WarehousingModel.objects.filter(currentdate=date).values_list('name', 'name_of_business', 'email', 'contact',
                                                                 'location_from', 'items_list')
    for warehouse_item in warehouse_items:
        writer.writerow(warehouse_item)
    return response

def view_404(request, exception):
    return render(request, 'booking/oops.html', {'title': 'Oops - FR Logistics'})
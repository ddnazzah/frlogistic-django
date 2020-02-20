from django.shortcuts import render


def index(request):
    return render(request, 'booking/index.html', {'title': 'Home - FR Logistics'})


def about(request):
    return render(request, 'booking/about.html', {'title': 'About - FR Logistics'})


def contact(request):
    return render(request, 'booking/contact.html', {'title': 'Contact - FR Logistics'})


def terms(request):
    return render(request, 'booking/terms.html', {'title': 'Terms and Conditions - FR Logistics'})


def book(request):
    return render(request, 'booking/book.html', {'title': 'Book Our Services - FR Logistics'})


def contact_confirm(request):
    context = {}
    context['name'] = request.POST.get('name', None)
    context['title'] = 'Success - FR Logistics'
    return render(request, 'booking/contact_confirm.html', context)

def book_confirm(request):
    context = {}
    context['title'] = 'Success - FR Logistics'
    return render(request, 'booking/book_confirm.html', context)

def oops(request):
    return render(request, 'booking/oops.html', {'title': 'Oops - FR Logistics'})

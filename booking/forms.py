# Authored by Alfred_Asare
from django import forms
from django.forms import ModelForm
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'id': 'name'}), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'id': 'mail'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Hi there, I\'m reaching out because I think we can collaborate...', 'id': 'message'}))


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryModel
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'id': 'mail'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Enter your contact', 'id': 'contact'}),
            'location_from': forms.TextInput(attrs={'placeholder': 'Enter GPS address of pickup point', 'id': 'from'}),
            'location_to': forms.TextInput(attrs={'placeholder': 'Enter GPS address of destination', 'id': 'to'}),
            'items_list': forms.Textarea(attrs={'placeholder': 'List your items (One item per line). Be as specific as possible', 'id': 'items'}),
        }
        fields = ['name', 'email', 'contact', 'location_from', 'location_to', 'items_list']


class SafeKeepingForm(forms.ModelForm):
    class Meta:
        model = SafeKeepingModel
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'id': 'name2'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email','id': 'mail2'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Enter your contact','id': 'contact2'}),
            'location_from': forms.TextInput(attrs={'placeholder': 'Enter GPS address of pickup point','id': 'from2'}),
            'date': DateInput(),
            'items_list': forms.Textarea(attrs={'placeholder': 'List your items (One item per line)','id': 'items2'}),
        }
        fields = ['name', 'email', 'contact', 'location_from', 'date', 'items_list']


class WarehousingForm(forms.ModelForm):
    class Meta:
        model = WarehousingModel
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'id': 'name3'}),
            'name_of_business': forms.TextInput(attrs={'placeholder': 'Enter name of business','id': 'business'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'id': 'mail3'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Enter your contact','id': 'contact3'}),
            'location_from': forms.TextInput(
                attrs={'placeholder': 'Enter GPS address of pickup point', 'id': 'from3'}),
            'items_list': forms.Textarea(
                attrs={'placeholder': 'List your items (One item per line)', 'id': 'items3'}),
        }
        fields = ['name', 'name_of_business', 'email', 'contact', 'location_from', 'items_list']

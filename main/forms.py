from django import forms
from django.forms.utils import ErrorList
from .models import Subscriber

class SubscriptionForm(forms.ModelForm):
	name = forms.CharField(
		label=' Имя ', 
		required=True, 
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control', 'placeholder':' Имя '})
	)

	telephone_number = forms.CharField(
		label=' Номер телефона ', 
		required=True,
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true', 'class':'form-control', 'placeholder':' Номер телефона '})
	)

	email = forms.CharField(
		label=' Эл. адрес. ', 
		required=True, 
		max_length=100,
		widget=forms.EmailInput(attrs={'required': 'true', 'class':'form-control', 'placeholder':' Эл. адрес. '})
	)

	class Meta:
		model = Subscriber
		exclude = ()
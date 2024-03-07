from django import forms
from . import models

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = models.Appointment
        fields = ['start_date', 'end_date', 'customer', 'dogs', 'services']
        labels = {
            'start_date': "Enter the start date",
            'end_date': "Enter the end date",
            'customer': "Select a customer",
            'dogs': "Select one or more dogs. User command + click to select multiple",
            'services': "Select one or more services. User command + click to select multiple",
        }
        widgets = {
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
            'customer': forms.Select(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
            'dogs': forms.SelectMultiple(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
            'services': forms.SelectMultiple(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
        }
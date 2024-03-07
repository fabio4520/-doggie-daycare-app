from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

# Appointment Views


class AppointmentListView(generic.ListView):
    model = models.Appointment
    form_class = forms.AppointmentForm


# Code Part 2.1 here

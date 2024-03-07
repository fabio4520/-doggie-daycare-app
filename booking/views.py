from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

# Appointment Views

class AppointmentListView(generic.ListView):
    model = models.Appointment
    form_class = forms.AppointmentForm

# Code Part 2.1 here
class AppointmentCreateView(generic.CreateView):
    model = models.Appointment
    form_class = forms.AppointmentForm
    success_url = reverse_lazy('index')

class AppointmentDetailView(generic.DetailView):
    model = models.Appointment

class AppointmentUpdateView(generic.UpdateView):
    model = models.Appointment
    form_class = forms.AppointmentForm
    success_url = reverse_lazy('index')

class AppointmentDeleteView(generic.DeleteView):
    model = models.Appointment
    success_url = reverse_lazy('index')

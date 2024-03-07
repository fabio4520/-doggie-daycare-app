import uuid
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils.http import urlencode
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError


class Customer(models.Model):

    # Fields
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Metadata
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ("first_name",)

    # Model Functions
    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Dog(models.Model):
    # Fields
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationships
    customers = models.ManyToManyField(Customer, blank=True)

    # Metadata
    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'
        ordering = ("first_name",)

    # Model Functions
    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Service(models.Model):
    # Fields
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Metadata
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ("name",)

    # Model Functions
    def __str__(self):
        return str(self.name)


class Appointment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    email_confirmation = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationships
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dogs = models.ManyToManyField(Dog)
    services = models.ManyToManyField(Service)

    # Metadata
    class Meta:
        ordering = ("start_date",)

    # Model Functions
    def __str__(self):
        return str(f"{self.customer} {self.start_date.strftime('(%Y/%m/%d)')}")
    def clean(self):
        # Verificar que la fecha de finalización sea mayor que la fecha de inicio
        if self.end_date <= self.start_date:
            raise ValidationError({'end_date': 'La fecha de finalización debe ser posterior a la fecha de inicio.'})
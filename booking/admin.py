from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

# Admin Login
# Username: admin
# Password: admin_password

from .models import Customer, Dog, Service, Appointment

class DogInline(admin.TabularInline):
    model=Dog.customers.through
    extra=1
class CustomerAdmin(admin.ModelAdmin):
    inlines = [DogInline]
    list_display = ('id', 'first_name', 'last_name', 'email', 'last_updated', 'created')  # Campos a mostrar en la lista
    fields = ('first_name', 'last_name', 'email')  # Campos editables
    list_filter = ('last_name',)  # Filtros por apellido
    search_fields = ('first_name', 'last_name', 'email')  # Búsqueda por nombre, apellido y email

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Dog)
admin.site.register(Service)
admin.site.register(Appointment)

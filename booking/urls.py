from django.urls import path
from .views import AppointmentListView, AppointmentCreateView, AppointmentDetailView, AppointmentUpdateView, AppointmentDeleteView

urlpatterns = [
    path('', AppointmentListView.as_view(), name='index'),
    # Code Part 2.2 here
    path('new/', AppointmentCreateView.as_view(), name='book_appointment'),
    path('<uuid:pk>/', AppointmentDetailView.as_view(), name='appointment_details'),
    path('<uuid:pk>/edit/', AppointmentUpdateView.as_view(), name='edit_appointment'),
    path('<uuid:pk>/delete/', AppointmentDeleteView.as_view(), name='delete_appointment'),
]

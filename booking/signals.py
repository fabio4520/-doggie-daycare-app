from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Appointment

def print_appointment_details(appointment):
    dogs = ', '.join([str(dog) for dog in appointment.dogs.all()])
    services = ', '.join([service.name for service in appointment.services.all()])
    print(f"""
    [
        To: {appointment.customer.email} 
        Subject: Appointment Confirmation Email
        Body: This email is to confirm that we have received your appointment! Your appointment details are below.
            Appointment time: {appointment.start_date.strftime('%Y-%m-%d'), "-", appointment.end_date.strftime('%Y-%m-%d')}
            Client: {appointment.customer}
            Dog(s): {dogs if dogs else "No dogs listed"}
            Service(s): {services if services else "No services listed"}
        We look forward to seeing you then!
    ]
    Admin: Email Confirmation Message Delivered to {appointment.customer}
    """)

@receiver(post_save, sender=Appointment)
def appointment_post_save(sender, instance, created, **kwargs):
    if created:
        # Marca el appointment para verificar si necesita imprimirse después, 
        # ya que inicialmente los M2M no estarán listos.
        instance._print_on_m2m_completed = True
        instance._m2m_changed = {'dogs': False, 'services': False}
        
@receiver(m2m_changed, sender=Appointment.dogs.through)
@receiver(m2m_changed, sender=Appointment.services.through)
def send_confirmation_email(sender, instance, action, **kwargs):
    if action == "post_add" and hasattr(instance, '_print_on_m2m_completed'):
        # Marca qué relación M2M ha cambiado.
        if sender == Appointment.dogs.through:
            instance._m2m_changed['dogs'] = True
        elif sender == Appointment.services.through:
            instance._m2m_changed['services'] = True
        
        # Verifica si ambas relaciones M2M han sido modificadas y si es necesario imprimir.
        if all(instance._m2m_changed.values()):
            print_appointment_details(instance)
            instance.email_confirmation = True
            instance.save(update_fields=['email_confirmation'])
            # Limpia los atributos temporales para evitar ejecuciones futuras en el mismo ciclo de vida.
            del instance._print_on_m2m_completed
            del instance._m2m_changed

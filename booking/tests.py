from django.test import TestCase
from .models import *


######################  Customer Model Tests ######################


class CustomerTest(TestCase):
    
    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="Fabio",
            last_name="Fiestas",
            email="fabioleofc@gmail.com"
        )

    def tearDown(self):
        self.customer.delete()

    def test_create(self):
        customer = Customer.objects.create(
            first_name="Fabio",
            last_name="Fiestas",
            email="fabioleofc@gmail.com"
        )
        self.assertIsInstance(customer, Customer)

    def test_read(self):
        self.assertEqual(self.customer.first_name, "Fabio")
        self.assertEqual(self.customer.last_name, "Fiestas")
        self.assertEqual(self.customer.email, "fabioleofc@gmail.com")

    def test_update(self):
        self.customer.first_name = "UpdatedName"
        self.customer.last_name = "UpdatedLastName"
        self.customer.email = "updatedfabioleofc@gmail.com"
        self.customer.save()

        updated_customer = Customer.objects.get(id=self.customer.id)
        self.assertEqual(updated_customer.first_name, "UpdatedName")
        self.assertEqual(updated_customer.last_name, "UpdatedLastName")
        self.assertEqual(updated_customer.email, "updatedfabioleofc@gmail.com")

    def test_delete(self):
        customer_id = self.customer.id
        Customer.objects.filter(id = customer_id).delete()
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(id=customer_id)


######################  Dog Model Tests ######################

class DogTest(TestCase):
    
    def setUp(self):
        self.dog = Dog.objects.create(
            first_name="Buddy",
            last_name="Doggo"
        )

    def tearDown(self):
        self.dog.delete()

    def test_create(self):
        dog = Dog.objects.create(
            first_name="Rex",
            last_name="Woof"
        )
        self.assertIsInstance(dog, Dog)

    def test_read(self):
        self.assertEqual(self.dog.first_name, "Buddy")
        self.assertEqual(self.dog.last_name, "Doggo")

    def test_update(self):
        self.dog.first_name = "UpdatedBuddy"
        self.dog.last_name = "UpdatedDoggo"
        self.dog.save()

        updated_dog = Dog.objects.get(id=self.dog.id)
        self.assertEqual(updated_dog.first_name, "UpdatedBuddy")
        self.assertEqual(updated_dog.last_name, "UpdatedDoggo")

    def test_delete(self):
        dog_id = self.dog.id
        Dog.objects.filter(id=dog_id).delete()
        with self.assertRaises(Dog.DoesNotExist):
            Dog.objects.get(id=dog_id)


######################  Service Model Tests ######################

class ServiceTest(TestCase):
    
    def setUp(self):
        self.service = Service.objects.create(
            name="Grooming",
            description="Full service grooming"
        )

    def tearDown(self):
        self.service.delete()

    def test_create(self):
        service = Service.objects.create(
            name="Walking",
            description="Daily walking service"
        )
        self.assertIsInstance(service, Service)

    def test_read(self):
        self.assertEqual(self.service.name, "Grooming")
        self.assertEqual(self.service.description, "Full service grooming")

    def test_update(self):
        self.service.name = "UpdatedGrooming"
        self.service.description = "Updated full service grooming"
        self.service.save()

        updated_service = Service.objects.get(id=self.service.id)
        self.assertEqual(updated_service.name, "UpdatedGrooming")
        self.assertEqual(updated_service.description, "Updated full service grooming")

    def test_delete(self):
        service_id = self.service.id
        Service.objects.filter(id=service_id).delete()
        with self.assertRaises(Service.DoesNotExist):
            Service.objects.get(id=service_id)



######################  Appointment Model Tests ######################

class AppointmentTest(TestCase):
    
    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="Fabio",
            last_name="Fiestas",
            email="fabioleofc@gmail.com"
        )
        self.dog = Dog.objects.create(
            first_name="Buddy",
            last_name="Doggo"
        )
        self.appointment = Appointment.objects.create(
            customer=self.customer,
            email_confirmation=True
        )
        self.appointment.dogs.add(self.dog)

    def tearDown(self):
        self.appointment.delete()
        self.dog.delete()
        self.customer.delete()

    def test_create(self):
        new_appointment = Appointment.objects.create(
            customer=self.customer,
            email_confirmation=True
        )
        self.assertIsInstance(new_appointment, Appointment)

    def test_read(self):
        self.assertEqual(self.appointment.customer, self.customer)
        self.assertTrue(self.appointment.email_confirmation)
        self.assertTrue(self.appointment.dogs.filter(id=self.dog.id).exists())

    def test_update(self):
        self.appointment.email_confirmation = False
        self.appointment.save()
        updated_appointment = Appointment.objects.get(id=self.appointment.id)
        self.assertFalse(updated_appointment.email_confirmation)

    def test_delete(self):
        appointment_id = self.appointment.id
        Appointment.objects.filter(id=appointment_id).delete()
        with self.assertRaises(Appointment.DoesNotExist):
            Appointment.objects.get(id=appointment_id)

    def test_appointment_services_relation(self):
        service1 = Service.objects.create(name="Bathing", description="Full bath")
        service2 = Service.objects.create(name="Nail Trimming", description="Trim nails")
        
        self.appointment.services.add(service1, service2)
        
        self.assertTrue(self.appointment.services.filter(id=service1.id).exists())
        self.assertTrue(self.appointment.services.filter(id=service2.id).exists())
        self.assertEqual(self.appointment.services.count(), 2)

    def test_appointment_date_validation(self):
        start_date = timezone.now()
        end_date = start_date - timezone.timedelta(days=1)  # Fecha de finalización anterior a la de inicio
        
        with self.assertRaises(ValidationError):
            Appointment.objects.create(
                customer=self.customer,
                start_date=start_date,
                end_date=end_date,
                email_confirmation=True
            ).clean()

    def test_appointment_deletion_on_customer_delete(self):
        # Asegurar que hay una cita existente
        self.assertTrue(Appointment.objects.filter(customer=self.customer).exists())
        
        # Eliminar el cliente
        customer_id = self.customer.id
        Customer.objects.filter(id = customer_id).delete()
        
        # Verificar que la cita también se haya eliminado
        self.assertFalse(Appointment.objects.filter(customer=self.customer).exists())


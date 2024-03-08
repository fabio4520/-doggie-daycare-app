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
    # Code Part 3.1 here
    pass


######################  Service Model Tests ######################


class ServiceTest(TestCase):
    # Code Part 3.1 here
    pass


######################  Appointment Model Tests ######################


class AppointmentTest(TestCase):
    # Code Part 3.1 here
    pass
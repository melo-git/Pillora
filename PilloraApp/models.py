from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    contact_number = models.CharField(max_length = 20) # could use PhoneNumberField from the django-phonenumber-filed package
    email = models.EmailField()
    address = models.TextField()


class ShippingContactAddress(models.Model):
    shipping_address = models.TextField()
    shipping_contact_number =models.CharField(max_length = 20)

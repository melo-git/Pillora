from django.db import models
from PilloraApp.models import Customer
from Mediventory import Staff, Product
# Create your models here.
class ShippingContactAddress(models.Model):
    shipping_addressId = models.BigAutoField(primary_key=True)
    shipping_address = models.TextField()
    shipping_contact_number =models.CharField(max_length = 20)
    customer = models.ForeignKey(Customer)

class Order(models.Model):
    order_date = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=15, decimal_places=5)
    customer = models.ForeignKey(Customer)
    order_status = models.CharField(max_length=50)

class Prescription(models.Model):
    prescription_form_file = models.FileField(upload_to='./uploads/prescriptions', null=True)
    prescription_text = models.TextField(null=True)
    customer = models.ForeignKey(Customer)
    staffId = models.ForeignKey(Staff)

class ProcessedPrescription(models.Model):
    prescriptionID = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    prescription_dosage = models.JSONField()

class OrderItems(models.Model):

    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)

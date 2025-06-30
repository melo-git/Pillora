from django.db import models

# Create your models here.
class Staff(models.Model):
    staffId = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    staff_role = models.CharField(max_length=50) 

class Stock(models.Model):
    pass
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    availability = models.CharField(max_length=20)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)







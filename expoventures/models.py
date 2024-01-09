from django.db import models

# Create your models here.
class User(models.Model):
    # The 'id' attribute is been ommited because the id field is implicitly added by Django for every model as the primary key. It's generally recommended to let Django handle the creation of the primary key automatically, as it simplifies the code and follows Django's convention over configuration philosophy.
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    # NOTE: In Django models, __init__ is often not explicitly defined because Django's base model class (models.Model) already provides a default implementation.
    # Also the purpose of the __str__ method is to provide a human-readable representation of the object when it is converted to a string or displayed in contexts like the Django admin interface.
    def __str__(self):
        return self.username
    
class Vendor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    amount = models.DecimalField(max_length=128, unique=True)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id}"
    
class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_length=10, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASADE)
    def __str__(self):
        return f"{self.name} is £{self.price}"

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product} in {self.order}"
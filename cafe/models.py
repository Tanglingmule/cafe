from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('main', 'Main'),
        ('snack', 'Snack'),
        ('drink', 'Drink'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} - £{self.price}"

class Customer(models.Model):
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.forename} {self.surname}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(MenuItem)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} - {self.customer} - {self.order_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-order_date']

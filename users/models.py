from django.db import models

# Create your models here

class client(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ]
    
    Fname = models.CharField(max_length=30)
    Sname = models.CharField(max_length=30)
    Email = models.CharField(max_length=70)
    Balance = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    phone = models.CharField(max_length=15)
    date = models.DateTimeField(null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='inactive')
    password = models.CharField(max_length=128)

   
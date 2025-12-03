from django.db import models
from django.core.validators import MinValueValidator

class Listing(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
        ('condo', 'Condo')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type =models.CharField(max_length=20, choices=PROPERTY_TYPES)
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    location =models.CharField(max_length=100)
        
    )
# Create your models here.

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=50)

    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    quality = models.DecimalField(
        default=0,
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    delivery_time = models.IntegerField()

    cost = models.DecimalField(max_digits=None, decimal_places=2)

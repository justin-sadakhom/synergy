from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Product(models.Model):
    """ A commodity that a Supplier wants to sell.

        Attributes:
            :name: Category it belongs to.
            :quantity: How much is available for a single order.
            :quality: Quality rating, from a scale of 0.0 to 5.0.
            :delivery_time: How long it takes to ship, in days.
            :cost: Cost per unit, in dollars.
    """

    name = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    quality = models.DecimalField(
        default=0,
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    delivery_time = models.IntegerField()
    cost = models.DecimalField(max_digits=None, decimal_places=2)

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm


# Create your models here.

class Item(models.Model):
    """ An abstract class representing an object with a name that can take the
    form of one or more units.

    Attributes:
        name (str): Name of the item.
        quantity (int): How much of the item there is.
    """

    name = models.CharField(max_length=30)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])


class Product(models.Model):
    """ A commodity that a Supplier wants to sell.

    Attributes:
        name: Category it belongs to.
        quantity: How much is available for a single order.
        quality: Quality rating, from a scale of 0.0 to 5.0.
        delivery_time: How long it takes to ship, in days.
        cost: Cost per unit, in dollars.
    """

    name = models.CharField(max_length=30)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    quality = models.DecimalField(
        default=0,
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    delivery_time = models.IntegerField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):

        name = self.name.capitalize()

        return "{0} – Price: ${1}, In Stock: {2}, {3}-day delivery" \
            .format(name, self.cost, self.quantity, self.delivery_time)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quality', 'quantity', 'delivery_time', 'cost']

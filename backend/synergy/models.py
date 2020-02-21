from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError


# Custom validators

def validate_name(name: str):

    if len(name) < 2:
        raise ValidationError('Name must have at least 2 characters')

    elif '  ' in name:
        raise ValidationError('Do not input more than 2 spaces in a row')


# Database models

class Item(models.Model):
    """ An abstract class representing an object with a name that can take the
    form of one or more units.

    Attributes:
        name (str): Name of the item.
        quantity (int): How much of the item there is.
    """

    name = models.CharField(max_length=30, validators=[validate_name])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        abstract = True


class Product(Item):
    """ A commodity available for purchase.

    Attributes:
        name (str): Name of the product.
        quantity (int): How much is available for a single order.
        cost (float): Cost per unit, in dollars.
        quality (float): Quality rating, from a scale of 0.0 to 5.0.
    """

    cost = models.DecimalField(max_digits=5, decimal_places=2)
    _quality = models.DecimalField(
        blank=True,
        default=0.0,
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value

    def update_quality(self) -> None:
        """ Set quality to a new value based on [...] """
        raise NotImplementedError

    def __str__(self):
        return '{0} – Price: ${1}, In Stock: {2}' \
            .format(name, self.cost, self.quantity)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'cost', '_quality']


class ClientLogin(models.Model):
    """ Information required for a client/supplier to login to the site.

    Attributes:
        username: Username to login.
        password: Password to login.

    """
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)

    def __str__(self):
        username = self.username.capitalize()
        return "Username - {0], Password - {1}"\
            .format(username, self.password)


class LoginForm(ModelForm):
    class Meta:
        model = ClientLogin
        fields = ['username', 'password']

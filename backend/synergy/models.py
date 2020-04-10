from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom validators

def validate_name(name: str):

    if len(name) < 2:
        raise ValidationError('Name must have at least 2 characters')

    for char in name:
        if not (char.isalpha() or char.isnumeric() or char == ' '):
            raise ValidationError('Name cannot have special characters')


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
        supplier (Supplier): The business supplying the product.
        _quality (float): Quality rating, from a scale of 0.0 to 5.0.
    """

    cost = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        validators=[MinValueValidator(0.0)]
    )

    supplier = models.ForeignKey(
        'synergy.Supplier',
        on_delete=models.CASCADE,
        null=True
    )

    _quality = models.DecimalField(
        default=0.0,
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        db_column='quality'
    )

    @property
    def quality(self):
        return self._quality

    def update_quality(self) -> None:
        """ Set quality to a new value based on [...] """
        raise NotImplementedError

    def __str__(self):

        name = str(self.name).capitalize()

        return '{0} – Price: ${1}, In Stock: {2}' \
            .format(name, self.cost, self.quantity)


class Request(Item):
    """ A request for a Product that fits certain criteria.

    Attributes:
        name (str): Name of the desired product.
        quantity (int): How much is wanted for a single order.
        min_budget (float): Minimum budget for the order.
        max_budget (float): Maximum budget for the order.
        client (Client): The business requesting the order.
        _min_quality (float): Minimum desired quality rating.
    """

    @property
    def min_quality(self):
        return self._min_quality

    # Fields that are only used to increase readability of budget.

    min_budget = models.DecimalField(
        default=0.0,
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0.0)]
    )

    max_budget = models.DecimalField(
        default=0.0,
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0.0)]
    )

    client = models.ForeignKey(
        'synergy.Client',
        on_delete=models.CASCADE,
        null=True
    )

    _min_quality = models.DecimalField(
        blank=True,
        default=0.0,
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )

    def __str__(self):

        name = str(self.name).capitalize()

        return '{0} – Budget: ${1}-${2}, Quantity: {3}' \
            .format(name, self.budget[0], self.budget[1], self.quantity)


class Business(models.Model):
    """ An abstract class representing a business using the website.

    Attributes:
        name (str): Title of the business.
        location (str): Where the business is located.
    """

    # Choices
    DOMESTIC = 'domestic'
    INTERNATIONAL = 'international'

    LOCATION_CHOICES = (
        (DOMESTIC, 'domestic'),
        (INTERNATIONAL, 'international')
    )

    # Fields
    name = models.CharField(max_length=20, validators=[validate_name])
    location = models.CharField('location', max_length=13,
                                choices=LOCATION_CHOICES)

    class Meta:
        abstract = True

    def __str__(self):

        name = str(self.name).capitalize()
        location = str(self.location).capitalize()

        return '{0} - {1}'.format(name, location)


class Supplier(Business):
    """ A business seeking to sell their goods.

    Attributes:
        _ethics_score: Ethics rating of the supplier on a scale of 0.0 to 5.0.
    """

    _ethics_score = 0

    def _update_ethics_score(self, new_score: float) -> None:
        """ Calculate and retrieve an updated ethics score. """
        raise NotImplementedError


class Client(Business):
    """ A business seeking a partnership with a supplier. """


class CustomUser(AbstractUser):

    END = 'END'
    SPL = 'SPL'
    MOP = 'MOP'
    GEN = 'GEN'
    SAM = 'SAM'
    OTH = 'OTH'

    JOB_FUNCTION_CHOICES = [
        (None, '- Select -'),
        (END, 'Engineering / Design'),
        (SPL, 'Supply Chain / Procurement / Logistics'),
        (MOP, 'Manufacturing / Operations'),
        (GEN, 'General Management'),
        (SAM, 'Sales & Marketing'),
        (OTH, 'Other')
    ]

    EXC = 'EXC'
    DIR = 'DIR'
    MNG = 'MNG'
    IND = 'IND'
    OWN = 'OWN'

    JOB_LEVEL_CHOICES = [
        (None, '- Select -'),
        (EXC, 'Executive'),
        (DIR, 'Director'),
        (MNG, 'Manager'),
        (IND, 'Individual Contributor'),
        (OWN, 'Owner')
    ]

    AERO = 'AERO'

    INDUSTRY_CHOICES = [
        (None, '- Select -'),
        (AERO, 'Aerospace & Defense'),
        (OTH, 'Other')
    ]

    CAN = 'CAN'

    COUNTRY_CHOICES = [
        (None, '- Select -'),
        (CAN, 'Canada'),
        (OTH, 'Other')
    ]

    # Fields

    job_function = models.CharField(
        max_length=3,
        choices=JOB_FUNCTION_CHOICES,
        null=True
    )

    job_level = models.CharField(
        max_length=3,
        choices=JOB_LEVEL_CHOICES,
        null=True
    )

    industry = models.CharField(
        max_length=4,
        choices=INDUSTRY_CHOICES,
        null=True
    )

    company_name = models.CharField(
        max_length=30,
        null=True
    )

    company_website = models.CharField(
        max_length=25,
        null=True
    )

    country = models.CharField(
        max_length=25,
        choices=COUNTRY_CHOICES,
        null=True
    )

    postal_code = models.CharField(
        max_length=7,
        null=True
    )

    def __str__(self):
        return self.first_name

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(CustomModel):
    NONE = 'na'
    OUNCE = 'oz'
    PINT = 'pt'
    QUART = 'qt'
    GALLON = 'gl'
    POUND = 'lb'
    BUNCH = 'bunch'
    BUSHEL = 'bu'

    UNIT_CHOICES = (
        (NONE, 'na'),
        (OUNCE, 'Ounce'),
        (PINT, 'Pint'),
        (QUART, 'Quart'),
        (GALLON, 'Gallon'),
        (POUND, 'Pound'),
        (BUNCH, 'Bunch'),
        (BUSHEL, 'Bushel'),
    )

    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=5,
                            choices=UNIT_CHOICES,
                            default=NONE)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __unicode__(self):
		return self.name

class Season(CustomModel):

    season = models.CharField(max_length=30)
    year = models.IntegerField()

    def __unicode__(self):
        return str(self.season) + ' ' + str(self.year)

class Week(CustomModel):
    season = models.ForeignKey(Season)
    number = models.IntegerField()
    product  = models.ManyToManyField(Product, through='Week_Product')

    class Meta:
        unique_together = ("season", "number")

    def __unicode__(self):
		return str(self.season.season) + ' ' + str(self.season.year) + ' Week ' + str(self.number)

class UserProfile(CustomModel):
    user = models.OneToOneField(User)

    street_address1 = models.CharField(max_length=64)
    street_address2 = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)

    def __unicode__(self):
        return self.user.username

class Week_Product(CustomModel):
    week = models.ForeignKey(Week)
    product = models.ForeignKey(Product)

class Order(CustomModel):
    user = models.ForeignKey(User)
    week = models.ForeignKey(Week)
    instructions = models.TextField()

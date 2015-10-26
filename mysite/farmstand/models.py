from django.db import models

# Create your models here.
class Products(models.Model):
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
    price = models.DecimalField(decimal_places=2)

    def __unicode__(self):
		return self.name
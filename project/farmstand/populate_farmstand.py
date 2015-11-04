import os

SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_PATH)

import django
django.setup()
from django.db.models import Min
from farmstand.models import Product, Season, Week, Week_Product

def add_product(name, quantity, unit, price):
    p = Product.objects.get_or_create(name=name,
                                        quantity=quantity,
                                        unit=unit,
                                        price=price
                                        )[0]
    return p

def add_season(season, year):
    s = Season.objects.get_or_create(season=season,
                                        year=year
                                        )[0]
    return s

def add_week(season_id, number):
    season = Season.objects.get(pk=season_id)

    try:
        # Check to see if object already exists.
        w = Week.objects.get(season_id=season_id,number=number)
    except:
        # If does not exist, exception is raised.
        # Create object.
        w = season.week_set.create(number=number)
    return w

def add_week_product(week_id, product_id):
    w = Week.objects.get(pk=week_id)
    p = Product.objects.get(pk=product_id)

    wp = Week_Product.objects.get_or_create(product=p, week=w)
    return wp

def populate():
    #min_season = Season.objects.all().aggregate(Min('id'))
    season = Season.objects.annotate(mins=Min('id'))[0].mins


    product_list = [
        ('Apple', 1, 'na', .5),
        ('Orange', 1, 'na', .5),
        ('Carrot', 1, 'bunch', 3.99),
        ('Maple syrup', 1, 'pint', 7),
        ('Eggs', 12, 'na', 2.99),
        ('Potatoes', 5, 'lb', 4.99)
        ]

    season_list = [
        ('Winter', 2015),
        ('Spring', 2015),
        ('Summer', 2015),
        ('Fall', 2015)
        ]

    week_list = [
        (season, 1),
        (season, 2),
        (season, 3),
        (season, 4),
        (season, 5)
        ]

    week_product_list = [
        (8, 14),
        (8, 15),
        (8, 16),
        (9, 17),
        (9, 18)
        ]

    for product in product_list:
        add_product(product[0], product[1], product[2], product[3])
    for season in season_list:
        add_season(season[0], season[1])
    for week in week_list:
        add_week(week[0], week[1])
    for week_product in week_product_list:
        try:
            add_week_product(week_product[0], week_product[1])
        except:
            print 'wp get_or_create failed'
# Start execution here!
if __name__ == '__main__':
    print "Starting Farmstand population script..."
    populate()

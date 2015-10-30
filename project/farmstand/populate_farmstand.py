import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()
from django.db.models import Min
from farmstand.models import Product, Season, Week

def add_product(name, quantity, unit, price):
    p = Product.objects.get_or_create(name=name,
                                        quantity=quantity,
                                        unit=unit,
                                        price=price
                                        )[0]
    p.save()
    return p

def add_season(season, year):
    s = Season.objects.get_or_create(season=season,
                                        year=year
                                        )[0]
    s.save()
    return s

def add_week(season_id, number):
    season = Season.objects.get(pk=season_id)

    try:
        w = Week.objects.get(season_id=season_id,number=number)
    except:
        w = season.week_set.create(number=number)
    return w
    # If w does not exist:

def populate():
    min_season = Season.objects.all().aggregate(Min('id'))
    season = Season.objects.annotate(min_season=Min('id'))
    min_season = season[0].min_season

    product_list = [
        ('Apple', 1, 'na', .5),
        ('Orange', 1, 'na', .5),
        ('Carrot', 1, 'bunch', 3.99),
        ('Maple syrup', 1, 'pint', 7),
        ('Eggs', 12, 'na', 2.99)
        ]

    season_list = [
        ('Winter', 2015),
        ('Spring', 2015),
        ('Summer', 2015),
        ('Fall', 2015)
        ]

    week_list = [
        (min_season, 1),
        (min_season, 2),
        (min_season, 3),
        (min_season, 4),
        (min_season, 5)
        ]

    for product in product_list:
        add_product(product[0], product[1], product[2], product[3])
    for season in season_list:
        add_season(season[0], season[1])
    for week in week_list:
        add_week(week[0], week[1])

# Start execution here!
if __name__ == '__main__':
    print "Starting Farmstand population script..."
    populate()

import csv
from dishsearchapp.models import Dish, Restaurant

def import_dishes_from_csv():
    with open('restaurants_small.csv', 'r') as csvfile:
        reader = list(csv.reader(csvfile))
        for i in range (1,501):
            dish_name = eval(reader[i][3]).keys()
            res_name = reader[i][1]
            loc = reader[i][2]
            if 'true' in reader[i][5]:
                rat = float(eval(reader[i][5].replace("true", "'true'"))['user_rating']['aggregate_rating'])
            else:
                rat = 0
            restaurant, _ = Restaurant.objects.get_or_create(name=res_name, location=loc, rating=rat)
            dish = Dish(name=dish_name, restaurant=restaurant)
            dish.save()

import_dishes_from_csv()

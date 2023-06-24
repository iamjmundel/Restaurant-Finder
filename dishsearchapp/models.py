from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rating = models.FloatField()

    def __str__(self, name, location, rating):
        return self.name, self.location, self.rating

class Dish(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

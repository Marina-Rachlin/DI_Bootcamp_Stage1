from django.db import models
import datetime


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'     

class Film(models.Model):
    title = models.CharField(max_length=150)
    release_date = models.DateTimeField(default=datetime.date.today)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='films')
    available_in_countries = models.ManyToManyField(Country, related_name='available_films')
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.film} {self.review_text}'





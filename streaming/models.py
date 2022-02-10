from django.db import models
from datetime import time


class Client(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.BigIntegerField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Payment(models.Model):
    date = models.DateTimeField()
    amount = models.FloatField()
    paymentMethod = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment of {self.amount} made by {self.client} on {self.date}"


class Subscription(models.Model):
    price = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client}'s account"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    genres = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    image = models.ImageField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, directed by {self.director}"


class Course(models.Model):
    title = models.CharField(max_length=200)
    modules = models.IntegerField(default=1)
    area = models.CharField(max_length=200)
    totalHours = models.DurationField(default=time(1))
    expert = models.CharField(max_length=200)
    image = models.ImageField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.area} by {self.expert}"


class TVShow(models.Model):
    title = models.CharField(max_length=200)
    season = models.IntegerField(default=1)
    episodes = models.IntegerField(default=1)
    director = models.CharField(max_length=200)
    image = models.ImageField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, directed by {self.director}"


class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    duration = models.DurationField()
    tvShow = models.ForeignKey(TVShow, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, from {self.tvShow}"


class Actor(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    birth = models.DateField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, from {self.movie}"


class Class(models.Model):
    title = models.CharField(max_length=200)
    transcript = models.CharField(max_length=2000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, from {self.course}"



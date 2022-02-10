from django.contrib import admin

from .models import Movie, Course, TVShow, Episode, Actor, Class, Client, Payment, Subscription

admin.site.register(Movie)
admin.site.register(Course)
admin.site.register(TVShow)
admin.site.register(Episode)
admin.site.register(Actor)
admin.site.register(Class)
admin.site.register(Client)
admin.site.register(Payment)
admin.site.register(Subscription)
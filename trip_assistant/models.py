# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Traveler(models.Model):
    """The user of Trip Assistant website."""

    username = models.CharField(max_length=24, unique=True)
    password = models.CharField(max_length=36)
    email = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class Trip(models.Model):
    """Info for a trip that belongs to a specific Traveler."""

    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    depart_date = models.DateField('departure date')
    return_date = models.DateField('return date')
    days = models.IntegerField(default=1)
    street_address = models.CharField(max_length=56, null=True)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256, null=True)
    country = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.city


@python_2_unicode_compatible
class Attraction(models.Model):
    """Business ids from Yelp API."""

    business_id = models.CharField(max_length=256)

    def __str__(self):
        return self.business_id


@python_2_unicode_compatible
class Recommendation(models.Model):
    """Record of attraction that has been recommended to a Traveler."""

    trip = models.ForeignKey(Trip)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    rec_value = models.IntegerField(null=True)  # value records if Traveler has voted rec up, down, or passed

    def __str__(self):
        return self.attraction

# Will add in classes to record a set itinerary for each day

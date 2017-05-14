# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Traveler(models.Model):
    """The user of Trip Assistant website."""

    username = models.CharField(max_length=24)
    password = models.CharField(max_length=36)
    email = models.CharField(max_length=64)


class Trip(models.Model):
    """Info for a trip that belongs to a specific Traveler."""

    traveler = models.ForeignKey(Traveler)
    depart_date = models.DateTimeField('departure date')
    return_date = models.DateTimeField('return date')
    days = models.IntegerField(default=1)
    destination = models.CharField(max_length=256)


class Attraction(models.Model):
    """Business ids from Yelp API."""

    business_id = models.CharField(max_length=256)


class Recommendation(models.Model):
    """Record of attraction that has been recommended to a Traveler."""

    trip = models.ForeignKey(Trip)
    attraction = models.ForeignKey(Attraction)
    rec_value = models.IntegerField(default=0)  # value records if Traveler has voted rec up, down, or passed


# Later, will add in classes to record a set itinerary for each day

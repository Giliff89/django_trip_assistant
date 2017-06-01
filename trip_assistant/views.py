# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import Http404, HttpResponse


def index(request):
    return render(request, 'trip_assistant/index.html')


def register(request):
    return HttpResponse("Create a new profile")


def login(request):
    return HttpResponse("Log in to your account")


def homepage(request, traveler):
    return HttpResponse("This is your personal homepage and news feed")


def traveler_profile(request, traveler):
    return HttpResponse("Welcome to your profile page, %s." % traveler)


def add_trip(request, traveler):
    return HttpResponse("%s add a new trip" % traveler)


def trip_profile(request, traveler, city):

    # TODO: Figure out how to map this to the specific user's trip by trip id,
    # may need to take in the trip.id instead of city and just return the city
    # try:
    #     trip = Trip.objects.get(pk=id)
    # except Trip.DoesNotExist:
    #     raise Http404("Trip does not exist")
    # return render(request, 'trip_assistant/detail.html', {'trip': trip})

    return HttpResponse("%s's trip to %s." % (traveler, city))

# Views needed: 1) Index 2) Sign up 3) Login 4) Logged-in Homepage
# 5) User profile 6) Add trip page 7) Trip profile 8) Itinerary builder
# 9) View friend profile

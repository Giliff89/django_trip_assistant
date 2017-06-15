# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# from django.http import Http404, HttpResponse


def index(request):
    return render(request, 'trip_assistant/index.html')


def register(request):
    return render(request, 'trip_assistant/register.html')


def login(request):
    return render(request, 'trip_assistant/login.html')


def homepage(request):
    return render(request, 'trip_assistant/homepage.html')


def traveler_profile(request):

    traveler = request.traveler.username

    return render(request, 'trip_assistant/traveler_profile.html', {'traveler': traveler})


def add_trip(request):

    return render(request, 'trip_assistant/add_trip.html')


def trip_profile(request):

    # TODO: Figure out how to map this to the specific user's trip by trip id,
    # may need to take in the trip.id

    # trip =

    # try:
    #     trip = Trip.objects.get(pk=id)
    # except Trip.DoesNotExist:
    #     raise Http404("Trip does not exist")
    # return render(request, 'trip_assistant/trip_profile.html', {'trip': trip})

    return HttpResponse("%s's trip to %s." % request.traveler.username)

# Views needed: 1) Index 2) Sign up 3) Login 4) Logged-in Homepage
# 5) User profile 6) Add trip page 7) Trip profile 8) Itinerary builder
# 9) View friend profile

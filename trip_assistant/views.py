# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import Http404, HttpResponse


def index(request):
    return render(request, 'trip_assistant/index.html')


def register(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'trip_assistant/register.html', {'error': 'Username has already been taken'})

        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
            login(request, user)
            return render(request, 'trip_assistant/register.html')

    else:
        return render(request, 'trip_assistant/register.html')


def loginview(request):
    if request.method == 'POST':

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            traveler = request.user.username
            return render(request, 'trip_assistant/traveler_profile.html', {'traveler': traveler}, {'flash': 'Logged in successfully!'})

        else:
            return render(request, 'trip_assistant/login.html', {'error': 'The Username and Password didn\'t match'})

    else:
        return render(request, 'trip_assistant/login.html')


def homepage(request):
    return render(request, 'trip_assistant/homepage.html')


@login_required
def traveler_profile(request):

    traveler = request.user.username

    return render(request, 'trip_assistant/traveler_profile.html', {'traveler': traveler})


@login_required
def add_trip(request):

    return render(request, 'trip_assistant/add_trip.html')


@login_required
def trip_profile(request):

    # TODO: Figure out how to map this to the specific user's trip by trip id,
    # may need to take in the trip.id

    # trip =

    # try:
    #     trip = Trip.objects.get(pk=id)
    # except Trip.DoesNotExist:
    #     raise Http404("Trip does not exist")
    # return render(request, 'trip_assistant/trip_profile.html', {'trip': trip})

    return HttpResponse("%s's trip to %s." % request.user.username)

# Views needed: 1) Index 2) Sign up 3) Login 4) Logged-in Homepage
# 5) User profile 6) Add trip page 7) Trip profile 8) Itinerary builder
# 9) View friend profile

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the trip assistant index.")


def traveler_profile(request, traveler):
    return HttpResponse("Welcome to your profile page, %s." % traveler)


def trip_profile(request, traveler, city):
    return HttpResponse("%s's trip to %s." % (traveler, city))

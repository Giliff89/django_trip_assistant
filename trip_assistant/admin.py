# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Traveler, Trip

admin.site.register(Traveler)

admin.site.register(Trip)

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<traveler>\w+)/?$', views.traveler_profile, name='traveler profile'),
    url(r'^profile/(?P<traveler>\w+)/(?P<city>\w+)/?$', views.trip_profile, name='trip profile'),

]

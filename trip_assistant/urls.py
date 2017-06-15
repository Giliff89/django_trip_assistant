from django.conf.urls import url

from . import views

app_name = 'trip assistant'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/(?P<traveler>\w+)/', views.homepage, name='homepage'),
    url(r'^profile/(?P<traveler>\w+)/?$', views.traveler_profile, name='traveler profile'),
    url(r'^profile/(?P<traveler>\w+)/(?P<city>\w+)/?$', views.trip_profile, name='trip profile'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
]

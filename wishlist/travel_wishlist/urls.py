from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),
    url(r'^visited/(?P<pk>\d+)/$', views.places_visited, name='places_visited'),
    url(r'^isvisited$', views.place_is_visited, name='place_is_visited'),
    url(r'^place/(?P<pk>\d+)/notvisited/$', views.place_list_information, name='place_list_information'),
]

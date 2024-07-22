from django.urls import include, path

from . import views


urlpatterns = [
    path('TestEvent', views.event_list, name='event_list'),
    path('testWeb', views.testWeb),
]
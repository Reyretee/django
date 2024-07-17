from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('main', views.home),
    path('cass', views.cass),
]
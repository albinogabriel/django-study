from django.urls import path
from gaming.views import home

urlpatterns = [
    path('', home),
]
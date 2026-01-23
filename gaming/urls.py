from django.urls import path
from . import views

app_name = 'gaming'

urlpatterns = [
    path('', views.home, name="home"),
    path('gamerhub/<int:id>/', views.gamerhub, name="gaming"),
]


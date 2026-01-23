from django.shortcuts import render
from utils.gaming.factory import make_game

# Create your views here.

def home(request):
    return render(request, 'gaming/pages/home.html',
    context = {
        'game': make_game(),
    })

def gamerhub(request, id):
    return render(request, 'gaming/pages/game-view.html',
    context = {
        'detail_page': True,
        'game': make_game(),
    })
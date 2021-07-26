# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def bigscreen(request):
    return render(request, 'draw/bigscreen.html')

def form(request):
    return render(request, 'draw/form.html')

def manager(request):
    return render(request, 'draw/manager.html')

def busser(request):
    return render(request, 'draw/busser.html')

def chef(request):
    return render(request, 'draw/chef.html')

def cashier(request):
    return render(request, 'draw/cashier.html')

def host(request):
    return render(request, 'draw/host.html')

def server(request):
    return render(request, 'draw/server.html')

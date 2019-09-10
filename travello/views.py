from django.shortcuts import render
from .models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleep'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Biryani First, Than Sherewani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.desc = 'Electronic City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750

    dests = [dest1,dest2,dest3]
    return render(request, 'index.html', {'dests':dests})

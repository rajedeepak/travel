from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination(1,"Delhi","images/destination_1.jpg","City that doesnt sleep", 100)
    dest2 = Destination(2,"Bangalore","images/destination_2.jpg","Garden City", 200)
    dest3 = Destination(3,"Mumbai","images/destination_3.jpg","Beachy", 300)

    return render(request,'index.html', {'dests': [dest1, dest2, dest3]})
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse



from .models import Flight, Passenger

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        for p in Flight.objects.raw('SELECT * FROM flights_flight'):
            print(p.origin, p.destination, p.duration)
        return render(request, "flights/index.html",
            {"flights": Flight.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def flights(request,flight_id):
    flight = Flight.objects.get(pk = flight_id)
    print("ooooooo")
    print(flight.origin, flight.destination, flight.duration)
    for p in flight.passengers.all():
        print(p.first, p.last, p.public)
    print(type(flight.passengers.all()))
    a = Passenger.objects.raw('SELECT * FROM flights_passenger where public = false')
    print(type(a))
    for p in a:
        print(p.first, p.last, p.public, p.flights)
    return render(request, "flights/flight.html" , {
        "flight" : flight,
        "passengers" : flight.passengers.all().exclude(public=False),
        # "passengers" : Passenger.objects.raw('SELECT * FROM flights_passenger as p JOIN flights_flights as f ON  where public = true and '),
        # "passengers" : Passenger.objects.raw('SELECT * FROM flights_passenger where public = true and id in (SELECT passenger_id FROM flights_passenger where flight_id = '+str(flight_id)+')'),
        "non_passengers" : Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST.get('passenger',False)))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights", args=(flight.id,)))
    
def search(request):
    if request.method == "POST":
        first = request.POST.get("first")
        last = request.POST.get("last")
        passenger = Passenger.objects.raw('SELECT * FROM flights_passenger where first like "%'+first+'%" and last like "%'+last+'%" and public = true')
        print("passenger")
        for p in passenger:
            print(p.first, p.last, p.public)
        return render(request, "flights/search.html", {
            "passengers": passenger
        })
    print(Passenger.objects.all())
    return render(request, "flights/search.html", {
        "passengers": Passenger.objects.all().exclude(public=False)
    })

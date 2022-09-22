from django.shortcuts import render

# Create your views here.
from cars.models import Car
from pages.models import Team


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('created_at').filter(is_featured=True)
    all_car = Car.objects.order_by('created_at')
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_car': all_car,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')

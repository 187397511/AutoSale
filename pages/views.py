from django.shortcuts import render
from .models import Team
from cars.models import Car

def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True)
    all_cars = Car.objects.order_by('-id')[:4]
    data = {
        'team': team,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    team = Team.objects.all()
    data = {
        'team': team,
    }
    return render(request, 'pages/about.html' , data)
def services(request):
    return render(request, 'pages/services.html')
def contact_us(request):
    return render(request, 'pages/contact_us.html')

# Create your views here.

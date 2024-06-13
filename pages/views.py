from django.shortcuts import render
from .models import Team

def home(request):
    team = Team.objects.all()
    data = {
        'team': team,
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

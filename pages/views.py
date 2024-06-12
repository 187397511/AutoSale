from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')
def services(request):
    return render(request, 'pages/services.html')
def contact_us(request):
    return render(request, 'pages/contact_us.html')

# Create your views here.

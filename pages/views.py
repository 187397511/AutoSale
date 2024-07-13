from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.db.models.functions import Upper
from decouple import config
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True)
    all_cars = Car.objects.order_by('-id')[:4]
    searched_color = Car.objects.values_list(Upper('colors'), flat=True).distinct()
    searched_model = Car.objects.values_list(Upper('model'), flat=True).distinct()
    searched_state = Car.objects.values_list(Upper('state'), flat=True).distinct()
    searched_year = Car.objects.values_list('year', flat=True).distinct()
    searched_condition = Car.objects.values_list(Upper('condition'), flat=True).distinct()
    searched_body_style = Car.objects.values_list(Upper('body_style'), flat=True).distinct()
    data = {
        'team': team,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'searched_color': searched_color,
        'searched_model': searched_model,
        'searched_state': searched_state,
        'searched_year': searched_year,
        'searched_condition': searched_condition,
        'searched_body_style': searched_body_style,
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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        admin_email = User.objects.get(is_superuser=True).email
        if phone:
            try:
                if len(phone)!=10 or not int(phone).is_integer():
                      messages.error(request,'enter correct phone no')
                      return redirect('contact us')

            except Exception as e:
                    print(e)
                    messages.error(request,'enter correct phone no')
                    return redirect('contact us')

        send_mail(
            subject,
            "Name:" + name + '\n' + "Email:" + email + '\n' + 'Phone:' + phone + '\n' + 'Message:-\n' + message,
            config('EMAIL_HOST_USER'),
            [admin_email],
            fail_silently=False,)
        messages.success(request, 'Thank you for contacting us, expect a reply soon')
        return redirect('contact us')
    return render(request, 'pages/contact_us.html')

# Create your views here.

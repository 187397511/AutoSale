from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from decouple import config
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        car_title = request.POST['car_title']
        car_id = request.POST['car_id']
        user_id = request.POST['user_id']
        customer_needs = request.POST['customer_needs']
        email = request.POST['email']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        if phone:
            try:
                if ('.' in phone) or len(phone)!=10 or not float(phone).is_integer():
                      messages.error(request,'enter correct phone no')
                      return redirect('/cars/'+car_id)

            except:
                    messages.error(request,'enter correct phone no')
                    return redirect('/cars/'+car_id)
            else:
                contact = Contact(first_name=first_name,last_name=last_name, car_title=car_title, customer_needs=customer_needs, email=email, state=state, car_ID=car_id, user_ID=user_id, phone=phone, message=message )
        else:
             contact = Contact(first_name=first_name,last_name=last_name, car_title=car_title, customer_needs=customer_needs, email=email, state=state, car_ID=car_id, user_ID=user_id, phone=0, message=message )
        contact.save()
        messages.success(request,'Your inquiry has been submitted')
        admin_email = User.objects.get(is_superuser=True).email
        send_mail(
            "New Inquiry",
            "New Inquiry for " + car_title,
            config('EMAIL_HOST_USER'),
            [admin_email],
            fail_silently=False,)

        return redirect('/cars/'+car_id)

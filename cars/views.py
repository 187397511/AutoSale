from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.functions import Upper

# Create your views here.
def cars(request):
    searched_color = Car.objects.values_list(Upper('colors'), flat=True).distinct()
    searched_model = Car.objects.values_list(Upper('model'), flat=True).distinct()
    searched_state = Car.objects.values_list(Upper('state'), flat=True).distinct()
    searched_year = Car.objects.values_list('year', flat=True).distinct()
    searched_condition = Car.objects.values_list(Upper('condition'), flat=True).distinct()
    searched_body_style = Car.objects.values_list(Upper('body_style'), flat=True).distinct()
    cars = Car.objects.order_by('-create_date') #gets all cars objects in reverse order of creation date
    paginator = Paginator(cars, 4) #shows 4 cars per page
    page_no = request.GET.get('page') #fetches page no
    try:
        paged_cars = paginator.page(page_no)
    except PageNotAnInteger: # if page is not an integer then show page 1
        paged_cars = paginator.page(1)
    except EmptyPage: # if page is out of bounds then show last page
        paged_cars = paginator.page(paginator.num_pages)

    data = {
        'cars': paged_cars,
        'searched_color': searched_color,
        'searched_model': searched_model,
        'searched_state': searched_state,
        'searched_year': searched_year,
        'searched_condition': searched_condition,
        'searched_body_style': searched_body_style,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    car_data = get_object_or_404(Car, pk=id)
    data = {
        'car_data': car_data,
    }
    return render(request, 'cars/car_detail.html', data)

def search_results(request):
    cars = Car.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
    if 'color' in request.GET:
        color = request.GET['color']
        if color:
            cars = cars.filter(colors__iexact=color)
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            cars = cars.filter(state__iexact=state)
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)
    if 'condition' in request.GET:
        condition = request.GET['condition']
        if condition:
            cars = cars.filter(condition__iexact=condition)
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if min_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    searched_color = Car.objects.values_list(Upper('colors'), flat=True).distinct()
    searched_model = Car.objects.values_list(Upper('model'), flat=True).distinct()
    searched_state = Car.objects.values_list(Upper('state'), flat=True).distinct()
    searched_transmission = Car.objects.values_list('transmission', flat=True).distinct()
    searched_condition = Car.objects.values_list(Upper('condition'), flat=True).distinct()
    searched_body_style = Car.objects.values_list(Upper('body_style'), flat=True).distinct()

    data = {
        'cars': cars,
        'searched_color': searched_color,
        'searched_model': searched_model,
        'searched_state': searched_state,
        'searched_transmission': searched_transmission,
        'searched_condition': searched_condition,
        'searched_body_style': searched_body_style,
            }

    return render(request, 'cars/search_results.html',data)

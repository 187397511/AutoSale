from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

year_choice = []
for year in range(1950, (datetime.now().year+1)):
    year_choice.append((year,year))

features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )


# Create your models here.
class Car(models.Model):
    car_title = models.CharField(max_length=255)
    colors = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    description = RichTextField()
    features = MultiSelectField(choices=features_choices, max_length=255)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    miles = models.IntegerField()
    state = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=datetime.now())
    mileage = models.IntegerField()
    passengers = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    no_of_owners = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    year = models.IntegerField(('year'),choices=year_choice)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="pics/cars/%Y/")
    photo1 = models.ImageField(upload_to="pics/cars/%Y/", blank=True)
    photo2 = models.ImageField(upload_to="pics/cars/%Y/", blank=True)
    photo3 = models.ImageField(upload_to="pics/cars/%Y/", blank=True)
    photo4 = models.ImageField(upload_to="pics/cars/%Y/", blank=True)


    def __str__(self):
        return self.car_title

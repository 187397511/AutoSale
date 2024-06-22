from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    car_title = models.CharField(max_length=255)
    customer_needs = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    state = models.CharField(max_length=100)
    car_ID = models.IntegerField()
    user_ID = models.IntegerField(blank=True)
    phone = models.BigIntegerField()
    message = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.first_name

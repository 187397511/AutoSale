from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    x_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)
    photo = models.ImageField(upload_to = 'pics/team/')

    def __str__(self):
        return self.first_name

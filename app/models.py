from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    gpx_file = CloudinaryField('', default='manual', resource_type='raw')
    date_created = models.DateTimeField(auto_now=True)
    distance = models.FloatField(default=0)
    start_time = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=1000, default='')

    class Meta:
        ordering = ["-date_created"]
    
    def __str__(self):
        return self.slug
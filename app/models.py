from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import modules.slug_helper as slug_helper

# Create your models here.

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    distance = models.FloatField(default=0)
    start_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=25,default='Trax Activity')
    description = models.CharField(max_length=1000, default='')
    gpx_file = CloudinaryField('', default='manual', resource_type='raw')
    likes = models.ManyToManyField(User, related_name='activity_like', blank=True)

    def gen(self, **kwargs):
        slug_str = "%s %s" % (self.title, self.user) 
        slug_helper.unique_slugify(self, slug_str) 
        super(Activity, self).save(**kwargs)
        #return self.slug

    class Meta:
        ordering = ["-date_created"]
    
    # def __str__(self):
    #     return self.slug

    def number_of_likes(self):
        return self.likes.count()    
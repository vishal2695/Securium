from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    pics = models.ImageField(null=True, blank=True, upload_to='pics')
    tym = models.DateTimeField(auto_now_add=True, auto_now=False)
    utym = models.DateTimeField(auto_now_add=False, auto_now=True)
    offer = models.BooleanField(default=False)
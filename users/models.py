from django.db import models

# Create your models here.
class User(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     phone = models.IntegerField(max_length=10)
     address_country = models.CharField(max_length=20)
     address_city = models.CharField(max_length=20)
     address_street = models.CharField(max_length=20)
     address_house_number = models.IntegerField(max_length=3)
     user_name = models.CharField(max_length=100)
     password = models.CharField(max_length=100)
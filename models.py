from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


class BookingDetails(models.Model):
    email = models.EmailField(max_length=255)
    mobile_no = models.IntegerField()
    location = models.TextField()
    category = models.TextField()
    work_hour = models.IntegerField()
    gender_preference = models.TextField(default="none")
    total_people = models.IntegerField()
    house_size = models.CharField(max_length=255, default="no comment")
    budget = models.CharField(max_length=255)
    comment = models.TextField()
    f_name = models.TextField()
    l_name = models.TextField()
    address = models.CharField(max_length=500)
    zipcode = models.IntegerField()

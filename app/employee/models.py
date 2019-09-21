from django.db import models
from phone_field import PhoneField


class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    device_name = models.CharField(max_length=20, blank=False)


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    mobile_number = PhoneField(unique=True, help_text='Contact number')
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING, related_name='device_id')

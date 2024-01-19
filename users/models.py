from django.db import models
from django.contrib.auth.models import User
from . constants import GENDER_TYPE

# Create your models here.


class UserAccountModels(models.Model):
    user = models.OneToOneField(
        User, related_name='account', on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    education = models.CharField(max_length=60)

    def __str__(self):
        return str(self.user.first_name)


class UserAddressModel(models.Model):
    user = models.OneToOneField(
        User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    def __str__(self):
        return str(self.user.email)

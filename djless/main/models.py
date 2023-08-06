from django.db import models


class Address(models.Model):
    address = models.TextField()


class Users(models.Model):
    user_name = models.CharField(max_length=20)
    user_surname = models.CharField(max_length=20)
    user_mail = models.CharField(max_length=20)
    user_address = models.ForeignKey(Address, on_delete=models.PROTECT)


# Create your models here.

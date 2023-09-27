from django.db import models


# Create your models here.
class Symptoms(models.Model):
    symp1 = models.CharField(max_length=250)
    symp2 = models.CharField(max_length=250)
    symp3 = models.CharField(max_length=250)
    symp4 = models.CharField(max_length=250)
    symp5 = models.CharField(max_length=250)

    # For save data as name
    def __str__(self):
        return self.symp1

class users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.TextField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email


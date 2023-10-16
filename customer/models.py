from django.db import models


# Create your models here.
def upload_path(instance, filname):
    return '/'.join(['customers', str(instance.name), filname])


class Customer(models.Model):
    name = models.CharField(max_length=200)
    industries = models.CharField(max_length=100)
    # image = models.ImageField(upload_to=upload_path, default="logo.png")

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=200)
    guardian = models.CharField(max_length=50)


class Menu(models.Model):
    menu = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)

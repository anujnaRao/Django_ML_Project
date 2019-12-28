from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    empid = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    addr = models.CharField(max_length=60)
    salary = models.IntegerField()
    phone = models.CharField(max_length=10)
    designation = models.CharField(max_length=10)

    def __str__(self):
        return self.name

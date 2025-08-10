from django.db import models


# Create your models here.

class Members(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    data_joined = models.DateField(null=True)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
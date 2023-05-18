from django.db import models

# Create your models here.

class student(models.Model):

    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TimeField(null=True, blank=True)
    # image = models.ImageField()
    file = models.FileField()


class Car(models.Model):

    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=60)


    def __str__(self):
        return self.car_name





# CRUD --> 1.Create, 2.READ, 3.update, 

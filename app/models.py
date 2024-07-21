from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
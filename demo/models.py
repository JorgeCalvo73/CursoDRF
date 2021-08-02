from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

class Book(models.Model):

    title = models.CharField(max_length=36, blank=False, unique= True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=4, default=0, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='cover/', blank=True)

    #Relaciones
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    #Lo que hacemos aquí es que, cada vez que queremos ver nuestro objeto en forma de String, nos saque su título para identificarlo mejor
    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=30)

    #Relación 1:N
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='authors')

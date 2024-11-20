from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.TextField()
    data=models.DateField()
    language=models.TextField()
    img=models.TextField()
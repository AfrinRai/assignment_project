from django.db import models

# Create your models here.
class Cover(models.Model):
   name = models.CharField(max_length=200)
   sid = models.IntegerField()
   course = models.CharField(max_length=100)
   uniName = models.CharField(max_length=50, default='default')


   def __str__(self):
       return self.name


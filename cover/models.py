from django.db import models

# Create your models here.
class Cover(models.Model):
   name = models.CharField(max_length=200)
   id = models.models.IntegerField(("50"))
   course = models.CharField(max_length=100)


   def __str__(self):
       return self.name


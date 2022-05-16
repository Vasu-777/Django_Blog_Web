from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50 )
    email = models.EmailField(max_length=50)   
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return str(self.name)

class Subscriber(models.Model):
    email = models.EmailField(max_length=50) 
    def __str__(self):
        return self.email       
        
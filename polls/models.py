from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=50)

    def _str_(self):
        return self.email+''+self.password
    
class Todo(models.Model):
    title = models.CharField(max_length=155)
    value = models.CharField(max_length=450)
    def __str__(self):
        return self.title+'  '+self.value
    
class contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    message=models





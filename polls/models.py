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
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    message=models.CharField(max_length=2000)
    def _str_(self):
        return self.email+' '+self.message
    

class Category(models.Model):
    name=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_created=True)

    class Meta:
        ordering=['-date_added']
    def __str__(self):
        return self.name



class Hotel(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField(500)
    category=models.ForeignKey(Category,related_name='categorie',on_delete=(models.CASCADE))
    image=models.CharField(max_length=5000)

    date_added=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-date_added']
    def __str__(self):
        return self.title+' '+str(self.price)
    
    

    


class Checkout(models.Model):
    email=models.EmailField(max_length=200)
    adresse=models.CharField(max_length=200)
    ville=models.CharField(max_length=200)
    pays=models.CharField(max_length=300,null=True)
    zipcode=models.CharField(max_length=300)
    nbpersonne=models.IntegerField(null=True,blank=True)
    nbenfant=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.email+' '+self.ville




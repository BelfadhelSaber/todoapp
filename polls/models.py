from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime



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
    price=models.IntegerField(null=True,blank=True)
    ## first of all price can't be float -50 dollar ! change this 
    ## price for the adult and kids 
    #price_adult = models.IntegerField(null=True,blank=True)
    #price_kids = models.IntegerField(null=True,blank=True)
    # bdel kyma theb tew ! 
    # 
    category=models.ForeignKey(Category,related_name='categorie',on_delete=(models.CASCADE))
    image=models.CharField(max_length=5000)
    description=models.CharField(max_length=5000,null=True)
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
    nbbebe=models.IntegerField(null=True,blank=True)
    select=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.email+' '+self.ville 

class Flight(models.Model):
    airline = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    departure_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.airline} | {self.departure} → {self.arrival}"

# models.py
from django.db import models

class Reserver_vol(models.Model):
    nbpersonne=models.CharField(max_length=200)
    Compagnie=models.CharField(max_length=200)
    Départ = models.CharField(max_length=100)
    Arrivée=models.CharField(max_length=300,null=True)
    date = models.DateTimeField(auto_now=True)
    Prix=models.DecimalField(max_digits=10, decimal_places=2)
    vol=models.CharField(max_length=500)
    Classe=models.CharField(max_length=500)
    
    def __str__(self):
        return self.nbpersonne+' '+self.Depart+' '+self.arrivee+' '+self.Prix+' '+self.vol+' '+self.Classe



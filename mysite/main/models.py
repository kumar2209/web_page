from django.db import models
from django.forms import ModelForm

# Create your models here.
class user_detail(models.Model): #this will create a table
    #now we will define columns in data base
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.first_name


class user_detail_form(ModelForm): #creating form from model class
    class Meta:
        model = user_detail
        fields = ['first_name', 'last_name', 'email','username','password']
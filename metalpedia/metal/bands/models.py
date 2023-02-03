from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=15,null=True,blank=True)
    formed = models.CharField(max_length=50,null=True,blank=True)
    notes = RichTextField(blank=True,null=True)
    approved = models.BooleanField('Approved',default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
        
class News(models.Model):
    title=models.CharField(max_length=100)
    text = RichTextField(blank=True,null=True)
    pub_date=models.DateTimeField('date published')
    
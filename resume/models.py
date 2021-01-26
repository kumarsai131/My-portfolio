from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Resume(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Age =models.CharField(max_length=30)
    Nationality=models.CharField(max_length=30)
    Freelance=models.CharField(max_length=30,default="Available")
    Address=models.CharField(max_length=30)
    Phone =models.CharField(max_length=11)
    Email=models.CharField(max_length=30)
    Linkedin=models.CharField(max_length=40)
    Languages=models.CharField(max_length=30)

class Post(models.Model):
    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=40)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title=models.CharField(max_length=40)
    backend=models.CharField(max_length=40)
    frontend=models.CharField(max_length=40)
    githuub=models.CharField(max_length=60)
    image=models.ImageField(upload_to='images/')
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title




from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Notes(models.Model):
    emailid=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=4000)

class Feedback(models.Model):
    emailid=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    feedback=models.CharField(max_length=400)

class Admin(models.Model):
    emailid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
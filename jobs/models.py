from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Tech_included(models.Model):
    Tech = models.TextField(max_length=20, blank=True, default=None)
     
    def __str__(self):
        return self.Tech

job_types = (
    ('Internship', 'Internship'),
    ('Freelance', 'Freelance'),
    ('Fulltime', 'Fulltime'),
    ('Temporary', 'Temporary'),

)


class Category(models.Model):
    Title = models.TextField( max_length=100)

    def __str__(self):
        return self.Title
    

class Company(models.Model):   
    Title = models.TextField( max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()

    def __str__(self):
        return self.Title



class Job(models.Model):
    employer = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=100)
    job_type = models.TextField(choices=job_types)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', default='')
    description  = models.TextField(blank=True, default='empty')
    location = models.TextField(max_length=100)
    thumbnail = models.ImageField(upload_to='job_thumbnail')
    experience_level = models.TextField(max_length=250)
    tech=  models.ManyToManyField(Tech_included)
    salary = models.IntegerField()
    is_featured = models.BooleanField(default=True)
    post_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title
    
 
# Create your models here

class Job_Application (models.Model):
    job = models.CharField(max_length=200, null=True)
    job_id = models.IntegerField()
    cv = models.FileField(upload_to='cvs', null= True)
    name =  models.CharField(max_length=200)
    phone=  models.CharField(max_length=200)
    email =  models.CharField(max_length=200)
    message =  models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True,null= True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
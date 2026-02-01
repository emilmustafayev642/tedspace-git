from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Partner(models.Model):
    image = models.ImageField(upload_to='partner_logos/')
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=2000, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    country = models.TextField(max_length=35)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position} at {self.company}"

class Subscriber(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

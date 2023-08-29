from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message= models.TextField()

    def __str__(self):
        return self.name




class StartUpImage(models.Model):
    title = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='banner_images')
    show =  models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class StoryImage(models.Model):
    title = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='story_images')
    show =  models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class FeaturedImage(models.Model):
    title = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='featured_images')
    show =  models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
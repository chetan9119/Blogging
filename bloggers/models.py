from django.db import models

# Create your models here.
class Blogger(models.Model):
    blogger_firstname = models.CharField(max_length=25, null=False)
    blogger_lastname = models.CharField(max_length=25, null=False)
    title = models.CharField(max_length=25, null=False)
    category = models.CharField(max_length=25, null=False)
    tags = models.CharField(max_length=25, null=False)
    article = models.TextField(max_length=2000, null=False)
    images = models.ImageField(upload_to='images', null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.blogger_firstname
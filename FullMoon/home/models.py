from django.db import models

# Create your models here.

class Herbs(models.Model):
    
        
    name = models.CharField(max_length=200)
    # description = models.CharField(max_length=300, null)
    uses = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000, default="...")
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Issues(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=200)
    herbs = models.ManyToManyField(Herbs)

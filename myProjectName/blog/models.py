from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/animals/')

    def __str__(self):
        return self.name

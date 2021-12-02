from django.db import models

# Create your models here.
class Contactx(models.Model):
    name=models.CharField(max_length=200)
    email=models.TextField()
    message=models.TextField()
    def __str__(self):
        return self.name
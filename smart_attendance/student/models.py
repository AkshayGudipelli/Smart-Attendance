from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=64)
    roll_no = models.CharField(max_length=15, unique=True)
    branch = models.CharField(max_length = 20)
    training_batch = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.full_name} - {self.roll_no}" 
    
        
from django.db import models
from student.models  import Student

# Create your models here.

class AttendanceRecord(models.Model):
    
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent')
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date =  models.DateField()
    scan_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    def __str__(self):
        return f"{self.student.full_name} - {self.status}  ({self.date})"
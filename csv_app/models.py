from datetime import datetime
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    company = models.CharField( max_length=100)
    Designation = models.CharField(max_length=100)
    DOJ = models.DateTimeField(default = datetime.now(),null =True)
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = "Employee"
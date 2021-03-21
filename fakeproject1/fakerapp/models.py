from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    first_name= models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    salary=models.IntegerField()
    company=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

class feedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()

    feedback=models.TextField()

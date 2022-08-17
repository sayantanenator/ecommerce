from django.db import models

# Create your models here.
#class Project(models.Model):
#    startDate=models.DateField()
#    endDate=models.DateField()
#    name=models.CharField(max_length=30)
#    assignedTo=models.CharField(max_length=20)
#    priority=models.IntegerField()

class Project(models.Model):
    productTitle=models.CharField(max_length=30)
    productCost=models.IntegerField()
    productOwner=models.CharField(max_length=30)

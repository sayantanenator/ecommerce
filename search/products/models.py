from django.db import models


class ModelformsProject(models.Model):
    #producttitle = models.CharField(db_column='productTitle', max_length=30)  # Field name made lowercase.
    #productcost = models.IntegerField(db_column='productCost')  # Field name made lowercase.
    #productowner = models.CharField(db_column='productOwner', max_length=30)  # Field name made lowercase.
    productTitle=models.CharField(max_length=30)
    productCost=models.IntegerField()
    productOwner=models.CharField(max_length=30)
    
    class Meta:
        managed = False
        db_table = 'modelforms_project'


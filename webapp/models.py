from django.db import models

class Donor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12,blank=True,null=True,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    dob = models.DateField()
    group = models.IntegerField()
    gender = models.IntegerField()

    def __str__(self):
        return self.name
    
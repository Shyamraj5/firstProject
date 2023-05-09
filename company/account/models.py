from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name 
    
class Manager(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    email=models.EmailField()
    qualifiaction=models.CharField(max_length=50)
    image=models.ImageField(upload_to='photos',null=True)
    
    def __str__(self) -> str:
        return self.first_name
    class Meta:
        db_table="Manager"  
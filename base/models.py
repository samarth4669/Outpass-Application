from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class data(models.Model):
    ChoiceList=(('Facultyadvisor','Facultyadvisor'),('Warden','Warden'),('Student-life coordinator','Student-life coordinator'))
    Name=models.CharField(max_length=25,default="-")
    studentid=models.CharField(max_length=25,default="-")
   
    facultymailid=models.CharField(max_length=40,default="-")
    facultyname=models.CharField(max_length=30,default="-")
    
    x=MultiSelectField(choices=ChoiceList,default="-")

class cont(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    message=models.TextField()
    date=models.CharField(max_length=20,default="-")
    time=models.CharField(max_length=20,default="-")
    facultyid=models.CharField(max_length=20,default="-")

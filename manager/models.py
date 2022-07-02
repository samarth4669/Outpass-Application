from django.db import models

# Create your models here.
class requesting(models.Model):
    opt=(('pending','pending'),('accepted','accepted'),('declined','declined'))
    starttime=models.DateTimeField()
    
    endtime=models.DateTimeField()
    reason=models.TextField()
    days=models.IntegerField()
    email=models.CharField(max_length=30)
    isfaculty=models.CharField(max_length=12,default="no")
    iswarden=models.CharField(max_length=12,default="no")
    islifecoordinator=models.CharField(max_length=12,default="no")
    status=models.CharField(max_length=25,choices=opt,default="pending")
    faculty=models.CharField(max_length=20,default="-")



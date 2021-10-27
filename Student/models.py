from django.db import models




class StudentModel(models.Model):
    name = models.CharField(' Name',max_length=200 )
    age = models.IntegerField('Age')
    address=models.TextField()
    email=models.EmailField(default="")
    pin=models.IntegerField(default=0)
    mob=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Weather(models.Model):
    humidity=models.IntegerField(max_length=50,blank=True);
    water=models.IntegerField(default=0,blank=True);
    light=models.IntegerField(default=0,blank=True);
    other=models.CharField(max_length=60,blank=True);
    ip=models.CharField(max_length=50,blank=True);
    time_occured=models.DateTimeField(auto_now_add=True)

    


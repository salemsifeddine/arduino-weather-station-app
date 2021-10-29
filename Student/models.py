from django.db import models


class Weather(models.Model):
    humidity=models.IntegerField(blank=True);
    water=models.IntegerField(default=0,blank=True);
    light=models.IntegerField(default=0,blank=True);
    other=models.CharField(max_length=60,blank=True);
    ip=models.CharField(max_length=50,blank=True);
    time_occured=models.DateTimeField(auto_now_add=True)

    


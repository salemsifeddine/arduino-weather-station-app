from .models import *
import serial
objectd={}

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def data_arduino(request):
    lightvaluesArr=[]
    sr=serial.Serial("com4",9600)
    arduino = sr.readline()
    dataarduino = str(arduino.decode("utf-8"))
    datamodified = dataarduino.strip()
    splitedarray=datamodified.split(',')
   

    for i in range(len(splitedarray)):

        key= splitedarray[i].split(':')[0]
        value= splitedarray[i].split(':')[1]
        
        objectd[key]=value.replace('\r\n','')
        
        # datasens.append(datamodified)
       

    sr.close()
    ip=get_ip(request)
    lightvalue = objectd['light']
    humvalue= objectd['humidity']
    water = objectd['water']

    
    
    weather, created= Weather.objects.get_or_create(light=lightvalue, humidity=humvalue
    ,water=int(water),ip=ip)
    weather.save()

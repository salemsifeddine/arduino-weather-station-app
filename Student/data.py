from .models import *
import serial
from pyfirmata import Arduino, util
import time
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


def roboticarm(request):
    


   
   

    # board.analog[0].disable_reporting()

    
    board = Arduino('com5')
    time.sleep(2)
    board.analog[0].write(50) 

    # Change to your port



    # while True:
    #     it = util.Iterator(board)

    #     it.start()
    #     board.analog[0].enable_reporting()
    #     tv1 = board.analog[0]
    #     time.sleep(1)
    #     print(tv1.read()* (1580/2))
       

  
   

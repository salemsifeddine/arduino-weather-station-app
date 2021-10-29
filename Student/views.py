from datetime import datetime
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .data import *
import serial
import datetime
from .form import  *
import datetime






def weathernow(request,template_name="weathernow.html"):
    
    try:
        data_arduino(request)
        weather=Weather.objects.all().last()

    except :
        weather=Weather.objects.all().last()
        
        
    
  
    
    hour=datetime.datetime.now().hour
    lightvaluesArr=[]
    labelvaluesArr=[]
    runvals=[]
    humvaluesArr=[]
    for lighval in Weather.objects.all():

        lightvaluesArr.append(lighval.light)
        humvaluesArr.append(lighval.humidity)
        
        intlabel=f"{lighval.time_occured.hour}.{lighval.time_occured.minute}{lighval.time_occured.second}"
        runvals.append({float(intlabel),lighval.water})
        labelvaluesArr.append(float(intlabel))

    
    context={"weather":weather, 'time':datetime.datetime.today(),'hour':int(hour),"rain":runvals,
    'dataarraylight':lightvaluesArr,"labelvaluesArr":labelvaluesArr,"humvaluesArr":humvaluesArr}
    return render(request,template_name,context)


realarray=[]
def fetch_sensor_values_ajax(request):
    data={}
    if request.is_ajax():
        com_port = request.GET.get('id', None)
            
        try:

            # sr=serial.Serial("COM9",9600)
            sr=serial.Serial(com_port,9600)
            st=str(sr.readline(),'utf-8')
            sr.close()
            listdata= st.split(',')
            realarray=[]
             
            for datum in listdata:
                target = datum.split(':')

                realobj={target[0]:int(target[1])}
                   
                realarray.append((realobj))

        except:
            pass
        
        data['result']=realarray
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)


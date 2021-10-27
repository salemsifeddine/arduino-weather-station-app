from datetime import datetime
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentForm
from .models import *
from .data import *
import serial



def add_student(request, template_name='student_add.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return  HttpResponse("ok saved")
        return redirect('Student:student_manage')
    return render(request, template_name, {'form':form})


def student_manage(request, template_name='student_manage.html'):
    std_data = StudentModel.objects.all() ###   select * from Student(table)
    data = {}
    data['object_list'] = std_data
    
    return render(request, template_name, data)


def student_edit(request, pk, template_name='student_add.html'):
    book= get_object_or_404(StudentModel, pk=pk)### select * from student where id=pk(parameterized id),pk means primary key
    form = StudentForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('Student:student_manage')
    return render(request, template_name, {'form':form})

def delete_student(request, pk):
    obj = get_object_or_404(StudentModel, pk=pk)
    obj.delete()
    return redirect('Student:student_manage')



def show_graph(request,template_name='live_graph.html'):
    

  
    # while True:
    #     sr=serial.Serial("COM4",9600)
    #     arduino = sr.readline()
    #     dataarduino = str(arduino[0:len(arduino)].decode("utf-8"))
    #     realdata=dataarduino
    #     print(realdata)

    #     sr.close()

    return render(request,template_name)


def show_graphh(request,template_name='live_graph_.html'):
    

  
    # while True:
    #     sr=serial.Serial("COM4",9600)
    #     arduino = sr.readline()
    #     dataarduino = str(arduino[0:len(arduino)].decode("utf-8"))
    #     realdata=dataarduino
    #     print(realdata)

    #     sr.close()

    return render(request,template_name)

from .form import  *
import datetime

def weathernow(request,template_name="weathernow.html"):
    
    try:
        data_arduino(request)
        weather=Weather.objects.all().last()
        
    except :
        weather=Weather.objects.all().last()
        
        
    
    # print(light.light)
    
    hour=datetime.datetime.now().hour
    lightvaluesArr=[]
    labelvaluesArr=[]
    humvaluesArr=[]
    for lighval in Weather.objects.all():
        lightvaluesArr.append(lighval.light)
        humvaluesArr.append(lighval.humidity)
        intlabel=f"{lighval.time_occured.hour}.{lighval.time_occured.minute}{lighval.time_occured.second}"
        labelvaluesArr.append(float(intlabel))

    


    context={"weather":weather, 'time':datetime.datetime.today(),'hour':int(hour),
    'dataarraylight':lightvaluesArr,"labelvaluesArr":labelvaluesArr,"humvaluesArr":humvaluesArr}
    return render(request,template_name,context)


def weather(request):
    form=''
    port= request.POST.get("key")
    
    if port:
        try:
            sr=serial.Serial("com4",9600)
            arduino = sr.readline()
            dataarduino = str(arduino[0:len(arduino)].decode("utf-8"))
            datamodified = dataarduino.strip()
            # datasens.append(datamodified)
            print(datamodified)
            sr.close()
            weather, created= Weather.objects.get_or_create(light=datamodified)
            weather.save()

            return redirect("weathernow")
           
        except :
            pass

    


    context={"form":form}
    return render(request, 'weather.html',context)


def weatherapi(request):
    data= json.loads(request.body.decode('utf-8'))
    idproduct=data['key']
    datamodified=''
    # action=data["action"]
    # if data["quantity"]:
    #     quantity=data["quantity"]
    # else:
    #     quantity=1
    # product= Product.objects.get(id=idproduct)
    # order, created= Order.objects.get_or_create(customer=request.user, complete=False)
    
    

    # if action == "add" and quantity:
    #    orderItem.quantity = (orderItem.quantity + quantity)
    # elif action == "remove":
    #     orderItem.quantity = (orderItem.quantity - 1)
    

    # totalItem=sum([item.quantity for item in OrderItem.objects.all()])
    
    # orderItem.save()
    
    # if orderItem.quantity <= 0 or action == "removecartproduct":
    #     orderItem.delete()
    #     #order.delete()
    datasens=[]
    try:
        sr=serial.Serial("COM4",9600)
        arduino = sr.readline()
        dataarduino = str(arduino[0:len(arduino)].decode("utf-8"))
        datamodified = dataarduino.strip()
        # datasens.append(datamodified)
        # print(datamodified)
        data['result']=datamodified
        sr.close()
           
    except :
        pass

    
    data_json = {
        'result':datamodified
    }

    return JsonResponse(data_json, safe=False)
    


def fetch_sensor_values_ajax(request):
    data={}
    datasens=[]
    if request.is_ajax():
            com_port = request.GET.get('id', None)
            # sensor_val=random.random() # auto random value if sendor is not connected , you can remove this line
            # sensor_data=[]
            # now=datetime.now()
            # ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))

            try:
                while True:
                    sr=serial.Serial("COM4",9600)
                    arduino = sr.readline()
                    dataarduino = str(arduino[0:len(arduino)].decode("utf-8"))
                    datamodified = dataarduino.strip()
                    datasens.append(datamodified)
                   
                    data['result']=datasens
                    # print(data['result'])
                    sr.close()
                # sr=serial.Serial("COM9",9600)
                # sr=serial.Serial("COM4",9600)
                # st=list(str(sr.readline(),'utf-8'))
                
                # sr.close()
                # sensor_val=str(''.join(st[:]))
                # if(sensor_val):
                #     sensor_data.append(str(sensor_val)+','+ok_date)
                # else:
                #     sensor_data.append(str(sensor_val)+','+ok_date)
            except Exception as e:
                    # sensor_data.append(str(sensor_val)+','+ok_date)
                    pass
            
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)


import json



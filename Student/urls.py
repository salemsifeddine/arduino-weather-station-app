from django.urls import path

from Student import views

app_name = 'Student'

urlpatterns = [
    # path('', views.add_student, name='add_student'),
 
    path('', views.weathernow, name='weathernow'),
    path('fetch_sensor_values_ajax/', views.fetch_sensor_values_ajax, name='fetch_sensor_values_ajax'),
    path("robotic-arm/", views.robot,name="robot")

]
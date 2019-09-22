from django.urls import path
from employee import views


urlpatterns = [
    path('employees/', views.EmployeeListCreate.as_view()),
    path('employees/<int:pk>/', views.EmployeeUpdateDelete.as_view()),
    path('devices/', views.DeviceListCreate.as_view()),
    path('devices/<int:pk>/', views.DeviceUpdateDelete.as_view()),
    path('empdevices/', views.EmployeeDeviceListCreate.as_view()),
    path('empdevices/<int:employee>/', views.EmployeeDeviceList.as_view()),
    path('empdevices/<int:employee>/<int:device>/', views.EmployeeDeviceDelete.as_view()),
]

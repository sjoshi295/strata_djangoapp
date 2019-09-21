from django.urls import path, re_path
from employee import views


urlpatterns = [
    path('employees/', views.EmployeeListCreate.as_view()),
    path('employees/<int:pk>/', views.EmployeeUpdateDelete.as_view()),
    path('devices/', views.DeviceListCreate.as_view()),
    path('devices/<int:pk>/', views.DeviceUpdateDelete.as_view()),
]

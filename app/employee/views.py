from employee.models import Employee, Device
from employee.serializers import EmployeeSerializer, DeviceSerializer
from rest_framework import generics


class EmployeeListCreate(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employee_id = self.kwargs['pk']
        return Employee.objects.filter(id=employee_id)


class DeviceListCreate(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class DeviceUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        device_id = self.kwargs['pk']
        return Device.objects.filter(id=device_id)

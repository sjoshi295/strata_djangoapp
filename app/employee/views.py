from employee.models import Employee, Device, EmployeeDevices
from employee.serializers import EmployeeSerializer, DeviceSerializer, EmployeeDeviceSerializer
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


class EmployeeDeviceListCreate(generics.ListCreateAPIView):
    serializer_class = EmployeeDeviceSerializer
    queryset = EmployeeDevices.objects.all()


class EmployeeDeviceList(generics.ListAPIView):
    serializer_class = EmployeeDeviceSerializer

    def get_queryset(self):
        employee_id = self.kwargs['employee']
        return EmployeeDevices.objects.filter(employee=employee_id)


class EmployeeDeviceDelete(generics.RetrieveDestroyAPIView):
    serializer_class = EmployeeDeviceSerializer
    lookup_field = 'employee'

    def get_queryset(self):
        employee_id = self.kwargs['employee']
        device_id = self.kwargs['device']
        return EmployeeDevices.objects.filter(employee=employee_id, device=device_id)

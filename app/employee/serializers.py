from rest_framework import serializers
from employee.models import Employee, Device, EmployeeDevices


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    # def create(self, validated_data):
    #     device_id = validated_data.pop('device', [])
    #     employee = super().create(validated_data)
    #     devices = Device.objects.filter(id=device_id)
    #     employee.device.add(*devices)
    #     return employee


class EmployeeDeviceSerializer(serializers.ModelSerializer):
    device = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Device.objects.all())
    employee = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Employee.objects.all())

    class Meta:
        model = EmployeeDevices
        fields = '__all__'
        depth = 2

    # def create(self, validated_data):
    #     device_id = validated_data.pop('device', [])
    #     employee_id = validated_data.pop('employee', [])
    #     employee_devices = super().create(validated_data)
    #     devices = Device.objects.filter(id=device_id)
    #     employees = Employee.objects.filter(id=employee_id) 
    #     employee_devices.device.add(*devices)

    #     return employee

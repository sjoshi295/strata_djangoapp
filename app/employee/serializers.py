from rest_framework import serializers
from employee.models import Employee, Device


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    device_id = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = '__all__'
        depth = 2

    def create(self, validated_data):
        device_id = validated_data.pop('device', [])
        employee = super().create(validated_data)
        devices = Device.objects.filter(id=device_id)
        employee.device.add(*devices)
        return employee

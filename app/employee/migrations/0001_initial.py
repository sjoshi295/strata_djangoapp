# Generated by Django 2.2.4 on 2019-09-22 17:43

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('device_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('mobile_number', phone_field.models.PhoneField(help_text='Contact number', max_length=31, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='device_id', to='employee.Device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_id', to='employee.Employee')),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-12 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managementAPI_app', '0002_employee_is_department_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_department_admin',
        ),
    ]

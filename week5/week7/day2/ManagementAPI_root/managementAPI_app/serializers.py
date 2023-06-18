from rest_framework import serializers
from managementAPI_app.models import Department, Employee, Task, Project



# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = '__all__'

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='DepartmentDetailAPIView')

    class Meta:
        model = Department
        fields = ['url', 'id', 'name', 'description']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='EmployeeDetailAPIView')

    class Meta:
        model = Employee
        fields = ['url', 'id', 'name', 'email', 'phone_number', 'department', 'projects']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')

    class Meta:
        model = Task
        fields = ['url', 'id', 'name', 'description', 'due_date', 'completed', 'project']

from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT)
from datetime import datetime

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        date_joined_param = self.request.query_params.get('date_joined')
        year, month, day = date_joined_param.split('-')
        if date_joined_param:
            queryset = queryset.filter(date_joined__year=year, 
                                       date_joined__month=month,
                                       date_joined__day=day)
        return queryset


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 

    



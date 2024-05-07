from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from django.db.models import Q
from .models import Company, Device,DeviceAssignment,DeviceLog,Employee
from .serializers import CompanySerializer, DeviceSerializer, DeviceAssignmentSerializer, DeviceLogSerializer, EmployeeSerializer

class Companyviewsets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class Employeeviewsets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class Deviceviewsets(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceAssignmentviewsets(viewsets.ModelViewSet):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer

class DeviceLogviewsets(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer



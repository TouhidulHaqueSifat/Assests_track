
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'companies',Companyviewsets)
router.register(r'employees',Employeeviewsets)
router.register(r'devices',Deviceviewsets)
router.register(r'deviceassignments',DeviceAssignmentviewsets)
router.register(r'devicelogs',DeviceLogviewsets)


urlpatterns = [
    path('',include(router.urls))
]
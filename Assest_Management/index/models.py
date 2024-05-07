from django.db import models
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name
    
class Device(models.Model):
    company = models.ForeignKey(Company,on_delete = models.CASCADE,null = True)
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.type} - {self.brand} {self.model}"
    
class DeviceAssignment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE )
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.device} assigned to {self.employee} from {self.start_date} to {self.end_date}"
    


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField(default=timezone.now)
    checkout_condition = models.TextField()
    return_time = models.DateTimeField(null=True, blank=True)
    return_condition = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Log for {self.device} checked out to {self.assigned_to}"


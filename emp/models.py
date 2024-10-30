from django.db import models

# Define your models without trying to import them from the same file
class Employee(models.Model):
    employeename = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

class Department(models.Model):
    department = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    contact = models.CharField(max_length=100)  # Ensure this field exists


class Truck(models.Model):
    day = models.CharField(max_length=10)
    departure_time = models.TimeField()
    tender = models.CharField(max_length=100)
    truck_number = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.truck_number
    
class Roster(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    roster_type = models.CharField(max_length=50)
    roster_status = models.CharField(max_length=50)
    notes = models.TextField()


from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class VehicleType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name   
    

class VehicleSize(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Vehicle(models.Model)  :
    vehicle_type  = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.DecimalField(max_digits=8, decimal_places=2)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehicle_type} - {self.id}"
    
class Rental(models.Model):
    rental_date = models.DateTimeField()  
    return_date = models.DateTimeField(null=True, blank=True)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f" Rental # {self.id}"
    

class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehicle_type} {self.vehicle_size}"


    
    




    


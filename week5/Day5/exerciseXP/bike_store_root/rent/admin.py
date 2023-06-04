from django.contrib import admin
from .models import Vehicle, Customer, RentalRate, Rental, VehicleType, VehicleSize

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Customer)
admin.site.register(RentalRate)
admin.site.register(Rental)
admin.site.register(VehicleType)
admin.site.register(VehicleSize)
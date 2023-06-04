import random
from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime, timedelta
from rent.models import Vehicle, Customer, Rental

class Command(BaseCommand):
    help = 'Populate rentals using faker'
    def handle(self, *args, **options):

        # vehicles = Vehicle.objects.all()
        vehicle_ids = Vehicle.objects.values_list('id', flat=True)

        
        # rented_vehicles = Rental.objects.filter(return_date__isnull=True).values_list('vehicle_id',flat =True)
        rentals_without_return_date = Rental.objects.exclude(return_date__isnull= False)
        print(type(rentals_without_return_date))
        for rental in rentals_without_return_date:
            valid_ids = set()
            valid_ids.add(rental.vehicle.id)

        print(valid_ids)    

            # vehicle_ids.remove[rental.vehicle.id - 1]
            # print(vehicle_ids)
       
        # not_ranted_vehicals_ids = []
        # for rental in rentals_with_return_date:
        #     not_ranted_vehicals_ids.append(rental.vehicle.id)
           
        # print(not_ranted_vehicals_ids)

        fake = Faker()

        # for _ in range(10):
        #     vehicle_id = random.choice(vehicle_ids)
        #     if vehicle_id not in 
        #     print(vehicle_id)
        

            # # rental_date = fake.datetimebetween(start_date = '-30d', end_date = 'today')
            # print(return_date)
            # return_date = None

            # if random.choice([True, False]):
            #     return_date = fake.date_between_dates(date_start=rental_date, date_end=datetime.now().date())


            # customer_ids = Customer.objects.values_list('id', flat=True)
            # random_customer_id = random.choice(customer_ids)    

            # Rental.objects.create(
            #     rental_date=rental_date,
            #     return_date=return_date,
            #     customer=random_customer_id, 
            #     vehicle=vehicle
            # )    



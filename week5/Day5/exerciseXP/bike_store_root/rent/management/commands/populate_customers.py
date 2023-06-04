from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from rent.models import Customer

class Command(BaseCommand):
    help = 'Populate the Customer table with fake data'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(20):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone_number = fake.phone_number()
            address = fake.address()
            city = fake.city() 
            country = fake.country()

            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                address=address,
                city=city,
                country=country
            )
            customer.save()

        self.stdout.write(self.style.SUCCESS('Fake data populated successfully.'))



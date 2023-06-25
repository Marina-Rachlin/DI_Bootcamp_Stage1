from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
   
    def __str__(self):
        return f'Profile: {self.user.username}'



class Category(models.Model):
    name = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    capacity = models.PositiveIntegerField() 

    def __str__(self):
        return self.name


class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.category.name} - {self.room_number}"
    
    
class RoomAmenities(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    
class UpcomingEvents(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    suitable_for_children = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class GuestDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    additional_details = models.TextField()

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_adults = models.PositiveIntegerField()
    num_kids = models.PositiveIntegerField(default=0)
    payment_status = models.CharField(max_length=20, default='Pending', choices=[('Paid', 'Paid'), ('Pending', 'Pending')])
    created_at = models.DateTimeField(auto_now_add=True)
    guest_details = models.OneToOneField(GuestDetails, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return f"Booking for Room {self.room.category.name - self.room.room_number}"

    def get_total_price(self):
        num_nights = (self.check_out_date - self.check_in_date).days
        return self.room.category.price_per_night * num_nights  
    

class Child(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()  

    
    
    # @staticmethod #TODO: work on this
    # def check_availability(request, category_id):
    #     category = Category.objects.get(id=category_id)
    #     rooms = Room.objects.filter(category=category)# all the rooms of the specific category
    #     available_rooms = []

    #     for room in rooms:
    #         if not Booking.objects.filter(room=room).exists():#it means that there are no bookings associated with the current room.
    #             available_rooms.append(room)

    #         if available_rooms:
    #             available_room = available_rooms.first()
    #         # Mark the room as temporarily booked
    #         # You can set a flag or update a field on the room model to indicate its temporary booking status

    #             context = {'category': category, 'room': available_room}
    #         else:
    #             context = {'category': category, 'room': None}

    #     return available_room
    


# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE) #??
#     rating = models.PositiveIntegerField()
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Review #{self.pk} by {self.user.username}"


# class Hotel(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField(max_length=100)
#     facebook_link = models.URLField(max_length=200, null=True, blank=True)
#     tiktok_link = models.URLField(max_length=200, null=True, blank=True)
#     instagram_link = models.URLField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return self.name

    

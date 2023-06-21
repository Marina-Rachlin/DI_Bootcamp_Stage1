from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Room)
admin.site.register(RoomAmenities)
admin.site.register(UpcomingEvents)
admin.site.register(Booking)

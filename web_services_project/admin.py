from django.contrib import admin
from .models import Client,Reservation,Voyage


admin.site.register(Client)
admin.site.register(Reservation)
admin.site.register(Voyage)
from django.contrib import admin

from .models import *

admin.site.register(Entity)
admin.site.register(Alcohol)
admin.site.register(AlcoholType)
admin.site.register(Shop)
admin.site.register(Offer)
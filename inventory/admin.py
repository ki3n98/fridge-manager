from django.contrib import admin

# Register your models here.
from .models import  ItemsDetails, Family, FamilyTag, FridgeContent

admin.site.register(ItemsDetails)
admin.site.register(Family)
admin.site.register(FamilyTag)
admin.site.register(FridgeContent)
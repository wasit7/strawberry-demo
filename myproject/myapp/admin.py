from django.contrib import admin

# Register your models here.
from myapp.models import Profile, Item, OrderItem

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)

class OrderItemAdmin(admin.ModelAdmin):    
    list_display = ('id','profile','item','quantity')
    list_display_links = ('id',)
    list_editable = ('item','quantity')
admin.site.register(OrderItem, OrderItemAdmin)
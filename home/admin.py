from home.models import  BookingDetails
from django.contrib import admin

from .models import *





class BookingDetailsAdmin(admin.ModelAdmin):
    list_display = ('email', 'mobile_no', 'location', 'category', 'work_hour', 'gender_preference',
                    'total_people', 'house_size', 'budget', 'comment', 'f_name', 'l_name', 'address', 'zipcode')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_no', 'service', 'message', 'date')



admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Sitter)
admin.site.register(OrderSitter)
admin.site.register(ShippingAddress)
admin.site.register(Contact, ContactAdmin)
admin.site.register(BookingDetails, BookingDetailsAdmin)


# admin.site.register(Contact, ContactAdmin)








# Register your models here.





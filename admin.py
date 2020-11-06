from django.contrib import admin
from app1.models import Contact, BookingDetails
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'desc', 'date')


class BookingDetailsAdmin(admin.ModelAdmin):
    list_display = ('email', 'mobile_no', 'location', 'category', 'work_hour', 'gender_preference',
                    'total_people', 'house_size', 'budget', 'comment', 'f_name', 'l_name', 'address', 'zipcode')


admin.site.register(Contact, ContactAdmin)
admin.site.register(BookingDetails, BookingDetailsAdmin)

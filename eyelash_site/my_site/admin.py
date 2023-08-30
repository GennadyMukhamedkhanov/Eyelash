from django.contrib import admin

from my_site.models import Time, Shedule, Service, Booking, User


# Register your models here.

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('user', 'shedule')
#     #list_display_links = ('status')
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'shedule')
    list_display_links = ()
    #search_fields = ('user_username',)
    list_editable = ('shedule',)
    list_filter = ('user', 'shedule')
    fields = ['shedule','user', ]

admin.site.register(Booking, BookingAdmin)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image')
    list_display_links = ('name', 'description',)



@admin.register(Shedule)
class SheduleAdmin(admin.ModelAdmin):

    list_display = ('service', 'date')
    list_filter = ('service', 'date')



@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date')
    ordering = ('start_date',)
    #list_display_links = ('start_date',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'phone', 'email', 'date_joined',)
    ordering = ('date_joined',)

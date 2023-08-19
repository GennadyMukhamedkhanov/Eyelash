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
    pass


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

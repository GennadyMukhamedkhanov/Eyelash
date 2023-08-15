from django.contrib import admin

from my_site.models import Time, Shedule, Service, Booking, User


# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Shedule)
class SheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

from .models import TruckModel, Truck, Cargo, CargoType


@admin.register(TruckModel)
class TruckModelAdmin(admin.ModelAdmin):
    pass


@admin.register(CargoType)
class CargoTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    pass


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo_type', 'weight', 'truck')
    list_filter = ('truck__truck_model__name',)

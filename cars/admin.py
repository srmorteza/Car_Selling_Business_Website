from django.contrib import admin
from .models import Car
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_title', 'color', 'model', 'year',
                    'body_style', 'fuel_type', 'is_featured')


admin.site.register(Car,CarAdmin)

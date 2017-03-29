from django.contrib import admin
from .models import LocationInfo, DustInfo
# Register your models here.


class LocationAdmin(admin.ModelAdmin):
	fieldsets = [
		('GPS_INFO',	{'fields' : ['latitude', 'longtitude']}),
		(None,	{'fields' : ['name']}),
	]
	list_display = ('latitude', 'longtitude', 'name')


admin.site.register(LocationInfo, LocationAdmin)
admin.site.register(DustInfo)
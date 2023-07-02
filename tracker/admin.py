from django.contrib import admin

# Register your models here.
from .models import Tracker
from .models import Driver
from .models import Chat

class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email',)

class TrackerAdmin(admin.ModelAdmin):
    list_display = ('car_name','mileage','driver','issue','describe_issues','date_added','date_edited')

class ChatAdmin(admin.ModelAdmin):
    list_display = ('driver','heading','date_added','date_edited')


admin.site.register(Tracker,TrackerAdmin)
admin.site.register(Driver,DriverAdmin)
admin.site.register(Chat,ChatAdmin)
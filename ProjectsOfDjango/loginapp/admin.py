from django.contrib import admin
from .models import LoginDetails,OmsAdmin
# Register your models here.

class ListLoginDetails(admin.ModelAdmin):
    list_display=('username','password') #displays the table in a list rather than as a objects

class ListOmsAdmin(admin.ModelAdmin):
    list_display=('brand','shipMethod','processingDays','processingDaysType','min','max','processingDate','availableToPromiseDate','cutOff')
admin.site.register(LoginDetails,ListLoginDetails) #registers model i.e database table in the admin page to view from the browser
admin.site.register(OmsAdmin,ListOmsAdmin)
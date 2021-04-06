from django.contrib import admin
from formularapp.models import MultiStepFormModel
# Register your models here.

class MultiStepFormModelAdmin(admin.ModelAdmin):
    list_display=('privat_oder_gewerbe','strom_oder_gas')

admin.site.register(MultiStepFormModel,MultiStepFormModelAdmin)

from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    list_filter = ('name',)
admin.site.register(Realtor, RealtorAdmin)
# Register your models here.

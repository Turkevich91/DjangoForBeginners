from django.contrib import admin
from .models import Animal


# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


admin.site.register(Animal, AnimalAdmin)
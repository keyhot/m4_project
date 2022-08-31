from django.contrib import admin
from .models import Bottle, BottlesCount


class BottleAdmin(admin.ModelAdmin):
    model = Bottle
    list_display = ["maker", "volume", "description", "expired"]
    list_editable = ["description", "expired"]
    fields = ["maker", "volume", "description", "expired", "orders"]


admin.site.register(Bottle, BottleAdmin)


class BottlesCountAdmin(admin.ModelAdmin):
    model = BottlesCount
    list_display = ["bottle", "count", "order"]
    list_editable = ["count"]
    fields = ["bottle", "count", "order"]


admin.site.register(BottlesCount, BottlesCountAdmin)

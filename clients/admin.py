from django.contrib import admin
from .models import Client, Order
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ["name", "address", "bottles_ordered", "active"]
    list_editable = ["active"]
    fields = ["name", "address", "bottles_ordered", "active", "photo", "user"]


admin.site.register(Client, ClientAdmin)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["name", "contacts", "created_at", "finished"]
    list_editable = ["contacts", "finished"]
    fields = ["name", "contacts", "created_at", "updated_at", "description", "finished"]
    readonly_fields = ["created_at", "updated_at",]


admin.site.register(Order, OrderAdmin)

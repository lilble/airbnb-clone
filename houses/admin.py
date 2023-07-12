from django.contrib import admin
from .models import House

# Register your models here.

@admin.register(House)  # decorator, admin 패널에 'House'라는 모델을 등록하고 싶다는 뜻
class HouseAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_month", "address", "pets_allowed")
    list_filter = ("price_per_month", "pets_allowed")
    search_fields = ("address",)
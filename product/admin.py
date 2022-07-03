from django.contrib import admin

from .models import ProductDetail, ProductCategory, AddToCard, Order, PaymentMode, city, Brand, Compare, Review, CourierPartner, TrackDetail
# Register your models here.

class AdminData(admin.ModelAdmin):
    list_display = ['product_name']
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(ProductDetail, AdminData)
admin.site.register(ProductCategory)
admin.site.register(AddToCard)
admin.site.register(Order)
admin.site.register(PaymentMode)
admin.site.register(city)
admin.site.register(Brand)
admin.site.register(Compare)
admin.site.register(Review)
admin.site.register(CourierPartner)
admin.site.register(TrackDetail)

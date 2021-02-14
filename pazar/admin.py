from django.contrib import admin
from .models import Category, Subcategory, Contact, Free_Listing, SaleItem, SaleBill ,PurchaseBill, PurchaseItem
from django.contrib.admin.options import ModelAdmin
from mapbox_location_field.admin import MapAdmin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon', 'image',]
    search_fields = ['name',]
admin.site.register(Category, CategoryAdmin)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'icon', 'image']
    search_fields = ['name',]
    list_filter = ['category',]
admin.site.register(Subcategory, SubcategoryAdmin)

class ContactAdmin(ModelAdmin):
    list_display = ['name', 'email', 'phone', 'msg', 'date']
    search_fields = ['name', 'email', 'phone']
admin.site.register(Contact, ContactAdmin)

from .models import FreeListingImage
class FreeListingImageAdmin(admin.StackedInline):
    model = FreeListingImage
admin.site.register(FreeListingImage)

class Free_ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'Business_Name', 'admin_photo', "Business_Category", "Business_Telephone", 'Business_Location', "Listed_at"]
    search_fields = ['Business_Name', 'Business_Category', 'Business_Subcategory']
    list_filter = ['Business_Name', 'Business_Category','Business_Subcategory']
    tag_fields = ["Business_Subcategory"]
    inlines = [FreeListingImageAdmin]

admin.site.register(Free_Listing, MapAdmin)

from .models import AdvertiseWithUsImage
class AdvertiseWithUsImageAdmin(admin.StackedInline):
    model = AdvertiseWithUsImage
admin.site.register(AdvertiseWithUsImage)

from .models import Advertise_with_Us
class Advertise_with_UsAdmin(admin.ModelAdmin):
    list_display = ['id', 'Business_Name', "Business_Category", "Business_Telephone", "Added_at"]
    search_fields = ['Business_Name', 'Business_Category', 'Business_Subcategory']
    list_filter = ['Business_Name', 'Business_Category','Business_Subcategory']
    tag_fields = ["Business_Subcategory"]
    inlines = [AdvertiseWithUsImageAdmin]

admin.site.register(Advertise_with_Us, MapAdmin)

from .models import Skill
admin.site.register(Skill)

from .models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'rate',]
    list_filter = ['rate',]
admin.site.register(Comment, CommentAdmin)

from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'shop', 'phone', 'address',]
    search_fields = ['name', 'shop', 'phone', 'address',]
    list_filter = ['shop',]
admin.site.register(Customer, CustomerAdmin)

from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'shop', 'admin_photo', 'price', 'offer_price',]
    search_fields = ['name', 'shop', 'price',]
    list_filter = ['shop', 'user']
admin.site.register(Product, ProductAdmin)

from .models import Stock
class StockAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin_photo', 'shop', 'user', 'date',]
    search_fields = ['name', 'user', 'shop', ]
    list_filter = ['shop', 'user',]
admin.site.register(Stock, StockAdmin)

from .models import Supplier
admin.site.register(Supplier)

from .models import PurchaseBill
admin.site.register(PurchaseBill)

from .models import PurchaseItem
admin.site.register(PurchaseItem)

from .models import SaleBill
admin.site.register(SaleBill)

from .models import SaleItem
admin.site.register(SaleItem)

from .models import QuotationBill
admin.site.register(QuotationBill)

from .models import QuotationItem
admin.site.register(QuotationItem)
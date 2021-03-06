from django.urls import path
from .import views
from .views import Free_ListingView, Advertise_With_UsView, DashboardView, CategoryDetailView, SubcategoryDetailView, ListingDetailView, shopEditView, shopDeleteView, customerDeleteView, customerEditView, skillEditView, skillDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home,  name="home"),
    path('about', views.about,  name="about"),
    path('contact', views.contact,  name="contact"),
    path('services', views.services, name="services"),
    path('categories', views.categories, name="all categories"),
    path('Search', views.Search, name="Search"),
    path('logout', views.logoutpage, name="logout"),
    path('free_listing', Free_ListingView.as_view(), name="Free Listing"), 
    path('Advertise_With_Us', Advertise_With_UsView.as_view(), name="Advertise With Us"),
    path('Dashboard/', views.DashboardView.as_view(), name="Dashboard"),
    path('ajax/load_subcategory', views.load_subcategory, name="ajax_load_subcategory"),
    path('category/<int:id>/<slug:slug>', CategoryDetailView.as_view() , name="category-detail"),
    path('subcategory/<int:id>/<slug:slug>', SubcategoryDetailView.as_view() , name="subcategory-detail"),
    path('listing/<int:id>/<slug:slug>', ListingDetailView.as_view(), name='listing-detail'),
    path('listing/<int:id>/<slug:slug>/addcomment', views.addcomment, name='addcomment'),
    path('shops', views.shopList, name="shop-list"),
    path('shop/<int:id>/<slug:slug>', views.shopDetail, name="shop-detail"),
    path('edit-shop/<int:id>/<slug:slug>', shopEditView.as_view(), name="edit-shop"),
    path('delete-shop/<int:id>/<slug:slug>', shopDeleteView.as_view(), name="delete-shop"),
    path('customers', views.customerList, name="customer-list"),
    path('add-customer', views.addCustomer, name="customer-add"),
    path('edit-customer/<int:id>/<slug:slug>', customerEditView.as_view(), name="edit-customer"),
    path('delete-customer/<int:id>/<slug:slug>', customerDeleteView.as_view(), name="delete-customer"),
    path('skills', views.skillList, name="skill-list"),
    path('add-skill', views.addSkill, name="add-skill"),
    path('edit-skill/<int:pk>', skillEditView.as_view(), name="edit-skill"),
    path('delete-skill/<int:pk>', skillDeleteView.as_view(), name="delete-skill"),
    path('myBlogs', views.blogList, name="blog-list"),
    path('products', views.ProductList, name="product-list"),
    path('add-product', views.AddProduct, name="product-add"),
    path('edit-product/<int:pk>', views.ProductEditView.as_view(), name="edit-product"),
    path('delete-product/<int:pk>', views.ProductDeleteView.as_view(), name="delete-product"),
    path('stocks', views.StockListView.as_view(), name="inventory"),
    path('add-stock', views.StockCreateView.as_view(), name="new-stock"),
    path('edit-stock/<int:pk>', views.StockUpdateView.as_view(), name="edit-stock"),
    path('delete-stock/<int:pk>', views.StockDeleteView.as_view(), name="delete-stock"),
    path('suppliers', views.SupplierListView.as_view(), name='supplier-list'),
    path('add-supplier', views.SupplierCreateView.as_view(), name='add-supplier'),
    path('edit-supplier/<int:pk>', views.SupplierEditView.as_view(), name='edit-supplier'),
    path('delete-supplier/<int:pk>', views.SupplierDeleteView.as_view(), name='delete-supplier'),
    path('suppliers/<name>', views.SupplierView.as_view(), name="supplier"),
    path('customers/<name>', views.CustomerView.as_view(), name="customer"),
    path('purchases', views.PurchaseView.as_view(), name="purchase-list"),
    path('new-purchase', views.SelectSupplierView, name="select-supplier"),
    path('new-purchase/<int:pk>', views.PurchaseCreateView.as_view(), name="add-purchase"),
    path('purchase-bill/<billNo>', views.PurchaseBillView.as_view(), name='purchase-bill'),
    path('purchase-delete/<int:pk>', views.PurchaseDeleteView.as_view(), name="delete-purchase"),
    path('sales', views.SaleView.as_view(), name='sale-list'),
    path('new-sale', views.SelectCustomerView, name='select-customer'),
    path('new-sale/<int:pk>', views.SaleCreateView.as_view(), name="add-sale"),
    path('sale-bill/<billNo>', views.SaleBillView.as_view(), name='sale-bill'),
    path('sale-delete/<int:pk>', views.SaleDeleteView.as_view(), name='delete-sale'),
    path('quotations', views.QuotationListView.as_view(), name='quotation-list'),
    path('new-quotation', views.SelectQuotationCustomerView, name='select-quote-customer'),
    path('new-quotation/<int:pk>', views.QuotationCreateView.as_view(), name='add-quotation'),
    path('quote-bill/<quoteNo>', views.QuotationView.as_view(), name="quotation-bill"),
    path('quote-delete/<int:pk>', views.QuotationDeleteView.as_view(), name="delete-quote"),
]

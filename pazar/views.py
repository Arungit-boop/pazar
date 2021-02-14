from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from .models import Contact, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView, DetailView, UpdateView, DeleteView, CreateView, ListView, View
from .forms import Free_ListingForm, CommentForm, PurchaseItemForm, SelectQuotationCustomerForm, QuotationItemForm, QuotationItemFormset
from .models import Free_Listing, Subcategory, FreeListingImage, AdvertiseWithUsImage, Category,Subcategory, Comment, Customer, Skill, Product, Stock, Supplier, SaleItem, SaleBill, PurchaseItem, PurchaseBill, QuotationItem, QuotationBill
from django.urls import reverse, reverse_lazy
from .forms import Advertise_With_UsForm, CustomerForm, SkillForm, ProductForm, SelectSupplierForm, PurchaseItemFormset, SupplierForm,SaleItemFormset, StockForm, SelectCustomerForm
from accounts.decorators import user_required, shop_owner_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Blog
from accounts.models import CustomUser, Profile
from django_filters.views import FilterView
from .filters import StockFilter
from django.forms import formset_factory, modelformset_factory
from num2words import num2words

# Create your views here.
def index(request):
    return render(request, 'pazar/index.html')

@login_required
def home(request):
    return render(request, 'pazar/home.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST. get('msg')

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(msg)<5:
            messages.warning(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, msg=msg, date=datetime.today())
            contact.save()
            messages.success(request, 'Your Queries has been Successfully Sent!')
    return render(request, 'pazar/contact.html')

def about(request):
    return render(request, 'pazar/about.html')

def services(request):
    return render(request,'pazar/services.html')

def categories(request):
    category = Category.objects.order_by('name')
    return render(request, 'pazar/categories.html', {'category':category})

def Search(request):
    return render(request, 'pazar/Search.html')

def logoutpage(request):
    logout(request)
    return redirect('logout')

@method_decorator([login_required, shop_owner_required], name='dispatch')
class Free_ListingView(SuccessMessageMixin, LoginRequiredMixin, FormView):
    template_name = "pazar/Free Listing.html"
    form_class = Free_ListingForm
    success_message = "Your Business %(Business_Name)s has been listed successfully!"

    def form_valid(self, form):
        listing = form.save(self.request.user)
        form.save_m2m()
        images = self.request.FILES.getlist('Business_Images')
        for i in images:
            FreeListingImage.objects.create(listing=listing,image=i)
        return super(Free_ListingView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("Free Listing")

@method_decorator([login_required, shop_owner_required], name='dispatch')
class Advertise_With_UsView(SuccessMessageMixin, LoginRequiredMixin, FormView):
    template_name = "pazar/Advertise With Us.html"
    form_class = Advertise_With_UsForm
    success_message = "Your Business %(Business_Name)s has been added successfully!"

    def form_valid(self, form):
        advertise = form.save(self.request.user)
        form.save_m2m()
        images = self.request.FILES.getlist('Business_Images')
        for i in images:
            AdvertiseWithUsImage.objects.create(advertise=advertise,image=i)
        return super(Advertise_With_UsView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("Advertise With Us")


class DashboardView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'pazar/dashboard.html'

    def get(self, request):
        labels = []
        data = []
        stockqueryset = Stock.objects.filter(user=request.user)
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.filter(user=request.user).order_by('-time')[:3]
        purchases = PurchaseBill.objects.filter(user=request.user).order_by('-time')[:3]
        context = {
            'labels':labels,
            'data':data,
            'sales':sales,
            'purchases':purchases
        }
        return render(request, self.template_name, context)

def load_subcategory(request):
    category_id = request.GET.get('Business_Category')
    subcategory = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'pazar/subcategory_dropdown_list_options.html', {'subcategory':subcategory})

def category_base(request):
    category = Category.objects.order_by('name')
    return render(request, 'category base.html', {'category':category})

class CategoryDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'pazar/subcategory.html'
    login_url = '/account/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        slug = self.kwargs['slug']
        name = Category.name
        categories = Category.objects.get(slug=slug, id=id)
        subcategory =  Subcategory.objects.filter(category__name=name)
        category = Category.objects.order_by("name")
        context['categories'] = categories
        context['subcategory'] = subcategory
        context['category'] = category
        return context

class SubcategoryDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'pazar/listing.html'
    login_url = '/account/login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        id = self.kwargs['id']
        slug = self.kwargs['slug']
        subcategories = Subcategory.objects.get(slug=slug, id=id)
        context['id'] = Subcategory.pk
        context['slug'] = Subcategory.slug
        context['subcategories'] = subcategories
        context['listing'] = Free_Listing.objects.filter(Business_Subcategory=subcategories)
        context['category'] = Category.objects.order_by("name")
        context["profile"] = profile
        return context
    
class ListingDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'pazar/business_list.html'
    login_url = '/account/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        slug = self.kwargs['slug']
        comments = Comment.objects.filter(listing_id=id)
        products = Product.objects.filter(shop_id=id)
        paginator = Paginator(comments, 3)
        page = self.request.GET.get('page')
        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)
        listing = Free_Listing.objects.get(pk=id,slug=slug)
        listing.view += 1
        listing.save()
        context['id'] = Free_Listing.pk
        context['slug'] = Free_Listing.slug
        context['listing'] = listing
        context['comments'] = comments
        context['products'] = products
        return context

def addcomment(request, id, slug):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.listing_id = id
            current_user = request.user
            data.commented_by_id = current_user.id
            data.save()
            messages.success(request, 'Your review has been sent. Thank you for your interest.')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

@login_required
def shopList(request):
    listing = Free_Listing.objects.filter(Listed_by=request.user)
    return render(request, 'pazar/shop list.html', {'listing':listing})

@login_required
def shopDetail(request, id, slug):
    listing = get_object_or_404(Free_Listing, id=id, slug=slug)
    customer = Customer.objects.filter(shop=listing, user=request.user)
    return render(request, 'pazar/shop detail.html', {'listing':listing, 'customer':customer})

class shopEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Free_Listing
    form_class = Free_ListingForm
    template_name = 'pazar/shop edit.html'
    success_url = reverse_lazy('shop-list')
    success_message = 'Your shop details has been updated!'

class shopDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Free_Listing
    template_name = 'pazar/shop delete.html'
    fields = '__all__'
    success_url = reverse_lazy('shop-list')
    success_message = 'Your shop has been deleted successfully!'

@login_required
def customerList(request):
    listing = Free_Listing.objects.filter(Listed_by=request.user)
    customer = Customer.objects.filter(user=request.user)
    return render(request, 'pazar/customer list.html', {'customer':customer, 'listing':listing})

@login_required
def addCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.user, request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, 'Customer added successfully!')
            return redirect('customer-list')
    else:
        form = CustomerForm(request.user)
    return render(request, 'pazar/add customer.html', {'form':form})

class customerEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'pazar/customer edit.html'
    success_message = 'Your customer details has been updated!'
    success_url = reverse_lazy('customer-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
class customerDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Customer
    template_name = 'pazar/customer delete.html'
    fields = '__all__'
    success_message = 'Your customer has been deleted successfully!'
    success_url = reverse_lazy('customer-list')

@login_required
def skillList(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'pazar/skill list.html', {'skills':skills})

@login_required
def addSkill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('skill-list')
    else:
        form = SkillForm()
    context = {
        'form':form
    }
    return render(request, 'pazar/add skill.html', context)

class skillEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'pazar/skill edit.html'
    success_message = 'Your skill has been updated!'
    success_url = reverse_lazy('skill-list')

class skillDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Skill
    template_name = 'pazar/skill delete.html'
    fields = '__all__'
    success_message = 'Your skill has been deleted successfully!'
    success_url = reverse_lazy('skill-list')
    
@login_required
def blogList(request):
    blog = Blog.objects.filter(author=request.user)
    return render(request, 'pazar/blog list.html', {'blog':blog})

@login_required
def ProductList(request):
    listing = Free_Listing.objects.filter(Listed_by=request.user)
    product = Product.objects.filter(user=request.user)
    return render(request, 'pazar/product list.html', {'product':product, 'listing':listing})

@login_required
def AddProduct(request):
    if request.method == "POST":
        form = ProductForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product-list')
    else:
        form = ProductForm(request.user)
    return render(request, 'pazar/add product.html', {'form':form})

class ProductEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'pazar/product edit.html'
    success_message = 'Your product has been updated!'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ProductDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'pazar/product delete.html'
    fields = '__all__'
    success_message = 'Your product has been deleted successfully!'
    success_url = reverse_lazy('product-list')

class StockListView(LoginRequiredMixin, FilterView):
    filterset_class = StockFilter
    template_name = 'pazar/inventory.html'
    paginate_by = 10

    def get_queryset(self):
        return Stock.objects.filter(user=self.request.user)

class StockCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'pazar/add stock.html'
    success_url = reverse_lazy('inventory')
    success_message = 'Stock has been created successfully!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class StockUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'pazar/edit stock.html'
    success_url = reverse_lazy('inventory')
    success_message = 'Stock has been updated successfully!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class StockDeleteView(LoginRequiredMixin, View):
    template_name = 'pazar/delete stock.html'
    success_message = 'Stock has been deleted successfully!'

    def get(self,request,pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object':stock})

    def post(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        stock.delete()
        messages.success(request, self.success_message)
        return redirect('inventory')

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'pazar/supplier list.html'
    paginate_by = 10

    def get_queryset(self):
        return Supplier.objects.filter(user=self.request.user)

class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy('supplier-list')
    success_message = 'Supplier has been created successfully!'
    template_name = 'pazar/add supplier.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class SupplierEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy('supplier-list')
    success_message = 'Supplier details has been updated successfully!'
    template_name = 'pazar/edit supplier.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class SupplierDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Supplier
    template_name = 'pazar/delete supplier.html'
    fields = '__all__'
    success_message = 'Your supplier has been deleted successfully!'
    success_url = reverse_lazy('supplier-list')

class SupplierView(LoginRequiredMixin, View):
    def get(self, request, name):
        supplierobj = get_object_or_404(Supplier, name=name)
        bill_list = PurchaseBill.objects.filter(supplier=supplierobj)
        page = request.GET.get('page', 1)
        paginator = Paginator(bill_list, 10)
        try:
            bills = paginator.page(page)
        except PageNotAnInteger:
            bills = paginator.page(1)
        except EmptyPage:
            bills = paginator.page(paginator.num_pages)
        context = {
            'supplier':supplierobj,
            'bills': bills
        }
        return render(request, 'pazar/supplier.html', context)

class PurchaseView(LoginRequiredMixin, ListView):
    model = PurchaseBill
    template_name = 'pazar/purchases list.html'
    context_object_name = 'bills'
    ordering = ['-time']
    paginate_by = 10

    def get_queryset(self):
        return PurchaseBill.objects.filter(user=self.request.user)

@login_required
def SelectSupplierView(request):
    form = SelectSupplierForm(request.user)
    if request.method == 'get':
        form = SelectSupplierForm(request.user, request.GET or None)
        return render(request, 'pazar/select supplier.html', {'form':form})
    if request.method == "POST":
        form = SelectSupplierForm(request.user, request.POST or None)
        if form.is_valid():
            supplierid = request.POST.get('supplier')
            supplier = get_object_or_404(Supplier, id=supplierid)
            shopid = request.POST.get('shop')
            shop = get_object_or_404(Free_Listing, id=shopid)
            return redirect('add-purchase', supplier.pk)
        return render(request, 'pazar/select supplier.html', {'form':form})
    return render(request, 'pazar/select supplier.html', {'form':form})

class PurchaseCreateView(LoginRequiredMixin, View):
    template_name = 'pazar/new purchase.html'

    def get(self, request, pk):
        formset = PurchaseItemFormset(request.GET or None ,form_kwargs = {'user':request.user})
        supplierobj = get_object_or_404(Supplier, pk=pk)
        context = {
            'formset':formset,
            'supplier':supplierobj
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        formset = PurchaseItemFormset(request.POST or None, form_kwargs={'user':request.user})
        supplierobj = get_object_or_404(Supplier, pk=pk)
        shopobj = get_object_or_404(Free_Listing, pk=pk)
        if formset.is_valid():
            billobj = PurchaseBill(supplier=supplierobj, shop=shopobj)
            billobj.user = request.user
            billobj.save()
            for form in formset:
                billitem = form.save(commit=False)
                billitem.user = request.user
                billitem.billNo = billobj
                stock = get_object_or_404(Stock, name = billitem.stock.name)
                billitem.totalPrice = billitem.perPrice * billitem.quantity
                stock.quantity +=billitem.quantity
                stock.user = request.user
                stock.save()
                billitem.save()
            messages.success(request, 'Purchased items have been registered successfully!')
            return redirect('purchase-bill', billNo=billobj.pk)
        formset = PurchaseItemFormset(request.GET or None, form_kwargs={'user':request.user})
        context = {
            'formset' :formset,
            'supplier':supplierobj
        }
        return render(request, self.template_name, context)

class PurchaseDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PurchaseBill
    template_name = 'pazar/delete purchase.html'
    success_url = reverse_lazy('purchase-list')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = PurchaseItem.objects.filter(billNo=self.object.pk)
        for item in items:
            stock = get_object_or_404(Stock, name=item.stock.name)
            if stock.delete():
                stock.quantity -= item.quantity
                stock.save()
        messages.success(self.request, 'Purchase Bill has been deleted successfully!')
        return super(PurchaseDeleteView, self).delete(*args, **kwargs)

class CustomerView(LoginRequiredMixin, View):
    def get(self, request, name):
        customerobj = get_object_or_404(Customer, name=name)
        bill_list = SaleBill.objects.filter(customer=customerobj)
        page = request.GET.get('page', 1)
        paginator = Paginator(bill_list, 10)
        try:
            bills = paginator.page(page)
        except PageNotAnInteger:
            bills = paginator.page(1)
        except EmptyPage:
            bills = paginator.page(paginator.num_pages)
        context = {
            'customer':customerobj,
            'bills':bills,
        }
        return render(request, 'pazar/customer.html', context)

class SaleView(LoginRequiredMixin, ListView):
    model = SaleBill
    template_name = 'pazar/sale list.html'
    context_object_name = 'bills'
    ordering = ['-time']
    paginate_by = 10

    def get_queryset(self):
        return SaleBill.objects.filter(user=self.request.user)

@login_required
def SelectCustomerView(request):
    form = SelectCustomerForm(request.user)
    if request.method == 'get':
        form = SelectCustomerForm(request.user, request.GET or None)
        return render(request, 'pazar/select customer.html', {'form':form})
    if request.method == "POST":
        form = SelectCustomerForm(request.user, request.POST or None)
        if form.is_valid():
            customerid = request.POST.get('customer')
            customer = get_object_or_404(Customer, id=customerid)
            shopid = request.POST.get('shop')
            shop = get_object_or_404(Free_Listing, id=shopid)
            return redirect('add-sale', customer.pk)
        return render(request, 'pazar/select customer.html', {'form':form})
    return render(request, 'pazar/select customer.html', {'form':form})

class SaleCreateView(LoginRequiredMixin, View):
    template_name = 'pazar/new sale.html'

    def get(self, request, pk):
        formset = SaleItemFormset(request.GET or None, form_kwargs={'user':request.user})
        customerobj = get_object_or_404(Customer, pk=pk)
        context = {
            'formset':formset,
            'customer':customerobj,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        formset = SaleItemFormset(request.POST or None, form_kwargs={'user':request.user})
        customerobj = get_object_or_404(Customer, pk=pk)
        shopobj = get_object_or_404(Free_Listing, pk=pk)
        if formset.is_valid():
            billobj = SaleBill(customer=customerobj, shop=shopobj)
            billobj.user = request.user
            billobj.save()
            for form in formset:
                billitem = form.save(commit=False)
                billitem.user = request.user
                billitem.billNo = billobj
                stock = get_object_or_404(Stock, name=billitem.stock.name)
                billitem.totalPrice = billitem.perPrice * billitem.quantity
                stock.quantity -= billitem.quantity
                stock.user = request.user
                stock.save()
                billitem.save()
            messages.success(request, 'Sold items have been registered successfully!')
            return redirect('sale-bill', billNo=billobj.pk)
        formset = SaleItemFormset(request.GET or None, form_kwargs={'user':request.user})
        context = {
            'formset':formset,
            'customer':customerobj
        }
        return render(request, self.template_name, context)

class SaleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SaleBill
    template_name = 'pazar/delete sale.html'
    success_url = reverse_lazy('sale-list')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = SaleItem.objects.filter(billNo=self.object.pk)
        for item in items:
            stock = get_object_or_404(Stock, name=item.stock.name)
            if stock.delete():
                stock.quantity += item.quantity
                stock.save()
        messages.success(self.request, 'Sale bill has been deleted successfully!')
        return super(SaleDeleteView, self).delete(*args, **kwargs)

class PurchaseBillView(LoginRequiredMixin, View):
    model = PurchaseBill
    template_name = 'pazar/purchase bill.html'

    def get(self, request, billNo):
        context = {
            'bill':PurchaseBill.objects.get(pk=billNo),
            'items':PurchaseItem.objects.filter(billNo=billNo),
        }
        return render(request, self.template_name, context)

    def post(self, request, billNo):
        context = {
            'bill':PurchaseBill.objects.get(pk=billNo),
            'items':PurchaseItem.objects.filter(billNo=billNo),
        }
        return render(request, self.template_name, context)

class SaleBillView(LoginRequiredMixin, View):
    model = SaleBill
    template_name = 'pazar/sale bill.html'

    def get(self, request, billNo):
        context = {
            'bill':SaleBill.objects.get(pk=billNo),
            'items':SaleItem.objects.filter(billNo=billNo),
        }
        return render(request, self.template_name, context)

    def post(self, request, billno):
        context = {
            'bill':SaleBill.objects.get(pk=billNo),
            'items':SaleItem.objects.filter(billNo=billNo),
        }
        return render(request, self.template_name, context)

class QuotationListView(LoginRequiredMixin, ListView):
    model = QuotationBill
    template_name = 'pazar/quotation list.html'
    context_object_name = 'quotations'
    ordering = ['-date']
    paginate_by = 10

    def get_queryset(self):
        return QuotationBill.objects.filter(user=self.request.user)

@login_required
def SelectQuotationCustomerView(request):
    form = SelectQuotationCustomerForm(request.user)
    if request.method == 'get':
        form = SelectQuotationCustomerForm(request.user, request.GET or None)
        return render(request, 'pazar/select quotation customer.html', {'form':form})
    if request.method == "POST":
        form = SelectQuotationCustomerForm(request.user, request.POST or None)
        if form.is_valid():
            customerid = request.POST.get('customer')
            customer = get_object_or_404(Customer, id=customerid)
            shopid = request.POST.get('shop')
            shop = get_object_or_404(Free_Listing, id=shopid)
            return redirect('add-quotation', customer.pk)
        return render(request, 'pazar/select quotation customer.html', {'form':form})
    return render(request, 'pazar/select quotation customer.html', {'form':form})

class QuotationCreateView(LoginRequiredMixin, View):
    template_name = 'pazar/new quotation.html'

    def get(self, request, pk):
        formset = QuotationItemFormset(request.GET or None, form_kwargs={'user':request.user})
        customerobj = get_object_or_404(Customer, pk=pk)
        context = {
            'formset':formset,
            'customer':customerobj
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        formset = QuotationItemFormset(request.POST or None, form_kwargs={'user':request.user})
        customerobj = get_object_or_404(Customer, pk=pk)
        shopobj = get_object_or_404(Free_Listing, pk=pk)
        if formset.is_valid():
            billobj = QuotationBill(customer=customerobj, shop=shopobj)
            billobj.user = request.user
            billobj.save()
            for form in formset:
                billitem = form.save(commit=False)
                billitem.user = request.user
                billitem.quoteNo = billobj
                billitem.totalPrice = billitem.perPrice * billitem.quantity
                numTotalPrice
                billitem.save()
            messages.success(request, 'Quotation has been created successfully!')
            return redirect('quotation-bill', quoteNo=billobj.pk)
        formset = QuotationItemFormset(request.GET or None, form_kwargs={'user':request.user})
        context ={
            'formset':formset,
            'customer':customerobj
        }
        return render(request, self.template_name, context)

class QuotationDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = QuotationBill
    template_name = 'pazar/delete quotation.html'
    fields = '__all__'
    success_message = 'Your Quotation has been deleted successfully!'
    success_url = reverse_lazy('quotation-list')

class QuotationView(LoginRequiredMixin, View):
    model = QuotationBill
    template_name = 'pazar/quotation.html'

    def get(self, request, quoteNo):
        context = {
            'quotes':QuotationBill.objects.get(pk=quoteNo),
            'items':QuotationItem.objects.filter(quoteNo=quoteNo)
        }
        return render(request, self.template_name, context)

    def post(self, request, quoteNo):
        context = {
            'quotes':QuotationBill.objects.get(pk=quoteNo),
            'items':QuotationItem.objects.filter(quoteNo=quoteNo)
        }
        return render(request, self.template_name, context)

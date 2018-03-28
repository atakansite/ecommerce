from django.shortcuts import render
from products.models import Products
from products.models import MainCategory
from products.models import SubCategory
# Create your views here.

def index(request):
    products = Products.objects.all()
    main_category = MainCategory.objects.all()
    sub_category = SubCategory.objects.all()

    return render(request, 'index.html', locals())
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .models import Product

# Create your views here.
def view_product_page(request):
    return render(request,'products/prouct.html')

def view_product_details(request):
    list_of_product= Product.objects.all()
    print(list_of_product)
    context_variable = {
        'products':list_of_product
    }
    return render(request,'products/product.html',context_variable)

def view_product_form(request):
    return render(request,'products/productform.html')

def view_productlist_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_Name = request.POST['product_Name']
        print(type(get_Name))
        get_Category = request.POST['product_Category']
        print(type(get_Category))
        get_Condition = request.POST['product_Condition']
        print(type(get_Condition))
        get_Price = request.POST['product_Price']
        print(type(get_Price))
        product = Product(Name=get_Name,Category=get_Category,Condition=get_Condition,Price=get_Price)
        product.save()
        return HttpResponse("Record Saved")
    else:
        return HttpResponse("Error record saving")
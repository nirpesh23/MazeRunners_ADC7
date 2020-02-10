from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .models import Product
    
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def view_product_page(request):
    return render(request,'products/prouct.html')


# Create your views here.
def view_homepage(request):
	return render(request,'homepage.html')

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



def search(request):
    if request.method=="POST":
        srh= request.POST['sea']
    
        if srh:
            match = Product.objects.filter(Name__icontains=srh)

            if match:
                return render(request,'products/productsearch.html', {"sr":match})
            else:
                return HttpResponse('Not successful')
        else:
            return('Not success')
    else:
        return render(request, 'products/productsearch.html')
        
    
def view_productdata_updateform(request,ID):
    print(ID)
    product_obj = Product.objects.get(id=ID)
    print(product_obj)
    context_varible = {
        'product':product_obj
    }
    return render(request,'product/productupdateform.html',context_varible)

def view_update_form_data_in_db(request,ID):
    product_obj = Product.objects.get(id=ID)
    print(product_obj)
    product_form_data = request.POST
    print(product_form_data)
    product_obj.Name = request.POST['Name']
    product_obj.Category =request.POST['Category']
    product_obj.Condition =request.POST['Condition']
    product_obj.Price = request.POST['Price']
    product_obj.save()

    return HttpResponse("Record Updated!!")

def view_register_user(request):
    if request.method =="GET":
        return render(request,'registration/register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse("Signup Successful")

def view_authenticate_user(request):
    if request.method =="GET":
        return render (request,'registration/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user)
            return render(request,"auth.html")
        else:
            return HttpResponse("Authentication Failed")  

    
def view_hello_world(request):
    pass

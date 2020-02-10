from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
import json

@csrf_exempt
def view_get_post_products(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        products = Product.objects.all()
        print("QuerySet objects => ",products)
        list_of_products = list(products.values("Name","Category","Condition","Price"))
        print("List of product objects => ",list_of_products)
        dictionary_name = {
        "products":list_of_products
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['Name'])
        print(python_dictionary_object['Category'])
        print(python_dictionary_object['Condition'])
        print(python_dictionary_object['Price'])
        Product.objects.create(Name=python_dictionary_object['Name'],Category=python_dictionary_object['Category'],Condition=python_dictionary_object['Condition'],Price=python_dictionary_object['Price'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("No List Working!!!!!")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        products = Product.objects.get(id = ID)
        print(type(products.Name))
        return JsonResponse({
            "id":products.id,
            "Name":products.Name,
            "Category":products.Category,
            "Condition":products.Condition,
            "Price":products.Price,

        
        })

    elif request.method=="PUT":
        guide=Product.objects.get(id=ID)
        python_dict_object = json.loads(request.body)
        guide.Name=python_dict_object['Name']
        guide.Category=python_dict_object['Category']
        guide.Condition=python_dict_object['Condition']
        guide.Price=python_dict_object['Price']
        guide.save()
        return JsonResponse({
        "message":" update your put data successfully!!!"
        })
    
    elif request.method=="DELETE":
        guide=Product.objects.get(id=ID)
        guide.delete()
        return JsonResponse({
        "message":" delete id successfully!!!!!!!!!1"
        })
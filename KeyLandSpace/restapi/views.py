from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
import json

@csrf_exempt
def view_get_post_products(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
       Product1 =Product.objects.all()
       print("QuerySet objects => ",Product1)
       list_of_Products = list(Product1.values("Name","Category"))
       print("List of products objects => ",list_of_Products)
       dictionary_name = {
        "Product1":list_of_Products
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
        Product.objects.create(Name=python_dictionary_object['Name'],Category=python_dictionary_object['Category'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        Product2 = Product.objects.get(id = ID)
        return JsonResponse({
            "id":Product2.id,
            "Name":Product2.Name,
            "Cataeory":Product2.Category,

        })
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })


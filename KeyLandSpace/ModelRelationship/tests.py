from django.test import TestCase
from ModelRelationship.models import Buyer,Seller,Customer,Product,Order_items,Order

# Create your tests here    
class ModelTestCase(TestCase):
    def setUp(self):
        b1 = Buyer.objects.create(Name="Rafayed" , Email="rafayed@gmail.com")
        b2 = Buyer.objects.create(Name= "Lipska" , Email="lipski@gmail.com")
        s1 = Seller.objects.create(Name="Alex" , Email="alex@gmail.com")

        c1 = Customer.objects.create(First_Name= "Jasmine", Last_Name="Lipska", Email="lipski@gmail.com", buyer=b1, seller=s1)

        def test_count_buyer(self):
            b1 = Buyer.objects.create(Name="Rafayed")
            self.assertEqual(b1.test_count_buyer(), 1)


        def test_count_seller(self):
            s1 = Seller.objects.create(Name="Alex")
            self.assertEqual(s1.count_seller(), 1)
from .models import Customer,Product

class test_customer_model(TestCase):
    def test_if_customer_name_is_blank(self):
        customer1= Customer.objects.create(First_Name="Nirpesh", Last_Name="Rajbhandari", Email="nirpesh@gmail.com")
        self.assertTrue(customer1.customer_name_blank_check())

    
    
    
class test_product_model(TestCase):  

    def test_brand_new_product_count_check(self):
        customer2=Customer.objects.create(Name="Samsung S9", Category="Phones", Condition="brand new", Price=70000)
        self.assertEqual(customer2.brand_new_product_count(),1)

    def test_used_product_count_check(self):
        customer2=Customer.objects.create(Name="Samsung S10", Category="Phones", Condition="used", Price=40000)
        self.assertEqual(customer2.brand_new_product_count(),1)

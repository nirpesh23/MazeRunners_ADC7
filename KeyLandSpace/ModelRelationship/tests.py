from django.test import TestCase
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
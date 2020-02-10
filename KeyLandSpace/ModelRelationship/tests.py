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
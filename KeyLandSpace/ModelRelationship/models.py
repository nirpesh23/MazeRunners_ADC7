from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Buyer(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Name} {self.Email}"
    
   
class Seller(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()


    
    def __str__(self):
        return f"{self.Name} {self.Email}"

   

class Customer(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
   

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name} email id is {self.Email} name of buyer is {self.buyer} and seller is {self.seller}"

    def customer_name_blank_check(self):
        if self.First_Name =="":
            return False 
        else:
            return True 

    def count_seller(self):
        return self.seller.all().count()

class Product(models.Model):
    Name = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    Condition = models.CharField(max_length=50)
    Price = models.FloatField()
   
    def __str__(self):
        return f"{self.Name} falls on {self.Category} it is {self.Condition} costing {self.Price}"

    def brand_new_product_count(self):
        product_brandnew_count=Product.objects.filter(Condition_is="brand new").count()
        return product_brandnew_count
    
    def used_product_count_check(self):
        used_product_count=Product.objects.filter(Condition_is="used").count()
        return used_product_count
    

class Order_items(models.Model):
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.TextField()
   
    def __str__(self):
        return f"{self.products.Name} is {self.description}"
 


class Order(models.Model):
    customer = models.ManyToManyField(Customer)
    product = models.ManyToManyField(Order_items)
    ordered_date = models.DateTimeField()
    
    def __str__(self):
        return f" {list(self.customer.all())} ordered {list(self.product.all())} in{self.ordered_date}"
        
        
    

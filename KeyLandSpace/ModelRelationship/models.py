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

    
    
    def count_buyer (self):
        return self.buyer.all().count()

    def count_seller(self):
        return self.seller.all().count()

class Product(models.Model):
    Name = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    Condition = models.CharField(max_length=50)
    Price = models.FloatField()
   
    def __str__(self):
        return f"{self.Name} falls on {self.Category} it is {self.Condition} costing {self.Price}"


    


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

    
    


        
        

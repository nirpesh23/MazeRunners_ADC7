from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    Customer_Id = models.IntegerField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Customer_Id} {self.First_Name} {self.Last_Name} {self.Email}"


class Product(models.Model):
    Name = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    Condition = models.CharField(max_length=50)
    Price = models.IntegerField()
    Quantity = models.ManyToManyField(Customer,blank=True,related_name='customers')
    
    
    
    def __str__(self):
        return f"From{self.Name} {self.Category} {self.Condition} {self.Price} {self.Quantity}"



class Order(models.Model):
    Order_Id = models.IntegerField(primary_key=True)
    Status = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="productstatus")

    
    

    def __str__(self):
        return f"{self.Order_Id} {self.Status} "
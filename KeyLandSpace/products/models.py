from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    Condition = models.CharField(max_length=50)
    Price = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.Name+" "+self.Condition
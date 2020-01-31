
from django.test import TestCase
from django.models import product
from django.contrib.auth.models import Permission,User
from .views import *

# Create your tests here.


class PermissionTest(TestCase):
  def Userpermission(self):
        user1=User.objects.filter(is_superuser=0)
        p2=Permission.objects.get(id=28)
        t1=test.objects.create(user=user1,permission=p2)
        self.assertTrue(t1.is_valid_flight())

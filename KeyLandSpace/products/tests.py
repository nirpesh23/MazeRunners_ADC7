
from django.test import TestCase
from django.models import product
from django.contrib.auth.models import Permission,User
from .views import *
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

# Create your tests here.


class PermissionTest(TestCase):
  def Userpermission(self):
        user1=User.objects.filter(is_superuser=0)
        p2=Permission.objects.get(id=28)
        t1=test.objects.create(user=user1,permission=p2)
        self.assertTrue(t1.is_valid_user())


class UserTest(TestCase):
   def test_user_count(self):
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    def test_authentication(self):
         user = authenticate(username='testuser', password='secret')
         self.assertTrue((user is not None) and user.is_authenticated)
from django.db import models

class User_Profile(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length = 200)
    email = models.EmailField(default = None)
    display_picture = models.FileField()

    def __str__(self):
        return self.fname

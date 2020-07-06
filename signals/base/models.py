from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  first_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, blank=True, null=True)
  phone = models.CharField(max_length=200, blank=True, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  profile_pic = models.ImageField(default="chow.jpeg", null=True, blank=True)
  facebook_link =  models.URLField(max_length=200, null=True, blank=True )
  github_link = models.URLField(max_length=200, null=True, blank=True)

  def __str__(self):
    return str(self.user)




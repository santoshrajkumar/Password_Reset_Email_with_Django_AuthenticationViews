from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from base.models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

  if created:
    Profile.objects.create(user=instance, first_name=instance.first_name,
                           last_name = instance.last_name, email = instance.email,
                          )
    print('Profile Created')


# post_save.connect(create_profile, sender=User)


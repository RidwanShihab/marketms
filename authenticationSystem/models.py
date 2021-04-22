


from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    prof_img=models.CharField(max_length=200, default='default.png')
    bio=models.CharField(max_length=255, null=True)
    birth_date=models.DateField(blank=True, null=True)
    hash=models.CharField(max_length=200, null=True)
    cover_photo = models.CharField(max_length=200, null=True)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

class captain(models.Model):
    captain=models.OneToOneField(User, on_delete=models.CASCADE)

class rider(models.Model):
    rider = models.OneToOneField(User, on_delete=models.CASCADE)

class rideHistory(models.Model):
    captain=models.OneToOneField(User, on_delete=models.CASCADE, unique=False)



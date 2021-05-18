


from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
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

class renter(models.Model):
    renter=models.OneToOneField(Profile, on_delete=models.CASCADE)



class paymentHistory(models.Model):
    payment=models.OneToOneField(User, on_delete=models.CASCADE, unique=False)

class shop(models.Model):
    shop=models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)

class apply(models.Model):

    details = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    shopname = models.CharField(max_length=45, blank=True, null=True)
    recommender= models.CharField(max_length=45, blank=True, null=True)

class bill(models.Model):
    biller = models.ForeignKey(User, on_delete=models.CASCADE,unique=False)
    method = models.CharField(max_length=45, blank=True, null=True)
    tid = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    amount = models.CharField(max_length=45, blank=True, null=True)
    month = models.CharField(max_length=45, blank=True, null=True)
    stat= models.CharField(max_length=45, blank=True, null=True)







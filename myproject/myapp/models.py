from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)
    email = models.EmailField()
    def __str__(self):
        return "%s"%(self.user)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('update_profile_signal: create a profile')

class Item(models.Model):
    UNIT_NAME_CHOICE = [ ("ชิ้น","ชิ้น"),("กร้ม","กร้ม") ]
    title = models.CharField(max_length=100)
    unit = models.CharField(max_length=5, choices=UNIT_NAME_CHOICE, default="ชิ้น")
    unit_price = models.DecimalField(max_digits=5, decimal_places=2) #999.99
    image = models.ImageField(upload_to='myimages') #from week05
    description = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return "%s"%(self.title)

class OrderItem(models.Model):
    profile = models.ForeignKey( Profile, on_delete=models.CASCADE)
    item = models.ForeignKey( Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return "profile:%s, item:%s, unit_price:%s quantity: %s %s"%(self.profile.name,self.item, self.item.unit_price, self.quantity, self.item.unit)
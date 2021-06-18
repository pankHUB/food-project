from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)    
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=5000,default="https://cdn.shopify.com/s/files/1/0533/2089/files/placeholder-images-image_large.png?format=jpg&quality=90&v=1530129081")


    def get_absolute_url(self):
        return reverse("food:detail" , kwargs={"pk":self.pk})
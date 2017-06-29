from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('departments',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=50,db_index=True)
    sub_description = models.CharField(max_length=200)

    def __str__(self):
        return self.sub_title

class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,unique=True)
    info = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
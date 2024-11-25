from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Watches(models.Model):
    gender = models.CharField(max_length=30)
    type = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True, help_text="Indicates whether the item is available or not.")
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Discount applied to the item, if any.")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.gender}<--->{self.type}'
    
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Watches"



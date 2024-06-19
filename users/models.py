from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLE =(
        ('client','client'),
        ('sallar','sallar'),
        ('admin','admin'),
    )
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default.jpg')
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    jobs = models.CharField(max_length=200, blank=True, null=True)
    user_role = models.CharField(max_length=100,choices=USER_ROLE,default="client")

    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_image', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.OneToOneField(Product,on_delete = models.CASCADE)
    quontity = models.PositiveBigIntegerField()

    def __str__(self) :
        return self.product.name

class Salar(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of = models.DateField(null=True,blank=True )

    def __str__(self):
        return self.user.username
    
class Client(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name
    

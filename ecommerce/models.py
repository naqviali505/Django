from django.db import models

class OrderUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    user = models.ForeignKey(OrderUser, on_delete=models.CASCADE)
    color = models.CharField(max_length=100,null=True)
    size = models.CharField(max_length=100,null=True)
    category = models.ForeignKey(ProductCategory,max_length=100,on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(OrderUser, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    payment_option=models.CharField(choices=[('COD','Cash on Delivery'),('Card','Card')],max_length=10)
    state = models.CharField(max_length=100,choices=[('draft','In Process'),('done','Delivered')],default='draft')
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
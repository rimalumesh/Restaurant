from django.db import models
import uuid

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=20)
    is_reserved = models.BooleanField(default=False,null=True)
    
    def __str__(self):
        return self.name
    
class Catagory(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE,related_name="items")
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    class ORDER_STATUS(models.TextChoices):
        PENDING = 'p', 'Preparing'
        PARTIALLY_SERVED = 'ps', 'Partially Served'
        SERVED = 's', 'Served'
        BILLED = 'b', 'Billed'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    table = models.ForeignKey(Table,on_delete=models.PROTECT,related_name='orders')
    status = models.CharField(max_length=2, choices = ORDER_STATUS,default=ORDER_STATUS.PENDING)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.table} -> {self.created_at}"
 
    
class OrderItem(models.Model):
    class ITEM_STATUS(models.TextChoices):
        PREPARING = 'p', 'Preparing'
        READY = 'r', 'Ready'
        SERVED = 's', 'Served'
    order = models.ForeignKey(Order,on_delete=models.PROTECT,related_name="items")
    menu_item = models.ForeignKey(MenuItem,on_delete=models.PROTECT,
    related_name = "order_items")
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=2, choices = ITEM_STATUS,default=ITEM_STATUS.PREPARING)
    
    def __str__(self):
        return f"{self.menu_item} x {self.quantity} qtys"
   
    
class OrderHistory(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE,related_name = "histories")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices = Order.ORDER_STATUS)
    
    def __str__(self):
        return f"{self.order} -> {self.status} at {self.created_at}"
    
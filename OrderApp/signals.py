from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from .models import Order,OrderHistory,OrderItem


# o1 = Order.objects.get()
# o1.status = 'r'
# o1.save() -> pre_save signal will be triggered and we can compare the previous status with the new status and create a new OrderHistory entry if there is a change in status.



@receiver(pre_save, sender = Order)
def handle_order_pre_save(sender,instance, **kwargs):
    if instance.pk:
        try:
            old_order = Order.objects.get(pk=instance.pk)
            instance._old_status = old_order.status
        except Order.DoesNotExist:
            instance._old_status = None
    else:
        instance._old_status = None
        
    
    
@receiver(post_save, sender = Order)
def handle_order_history_creation(sender,**kwargs):
    order = kwargs.get('instance')
    
    if order._old_status != order.status:
        OrderHistory.objects.create(
            order = order,
            status = order.status
        )
    
@receiver(post_save, sender = OrderItem)
def handle_auto_order_status_update(sender, **kwargs):
    order_item = kwargs.get('instance')   
    if order_item.status == OrderItem.ITEM_STATUS.SERVED:
        all_items = OrderItem.objects.filter(order = order_item.order)
        for item in all_items:
            if item.status != OrderItem.ITEM_STATUS.SERVED:
                order_item.order.status = Order.ORDER_STATUS.PARTIALLY_SERVED
                order_item.order.save()
                break
        else:
            print("Yes all items are served")
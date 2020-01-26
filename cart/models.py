from django.db import models

# Create your models here.
class Cart(models.Model):
    product_id = models.IntegerField(name='product_id')
    customer_id = models.IntegerField(name='customer_id')
    qty = models.IntegerField(name = "qty")
    created_at = models.DateTimeField('Created Date')
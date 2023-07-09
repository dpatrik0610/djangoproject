from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    value = models.IntegerField()
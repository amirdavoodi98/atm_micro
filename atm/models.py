from django.db import models

# Create your models here.
class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    source_account_id = models.IntegerField()
    destination_account_no = models.CharField(max_length=100)
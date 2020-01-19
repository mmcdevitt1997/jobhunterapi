from djmoney.models.fields import MoneyField
from django.db import models

class JobModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    job_link = models.CharField(max_length=150)
    active = models.BooleanField(initial=True)


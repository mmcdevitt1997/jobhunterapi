from django.db import models
from .jobmodel import JobModel

class StageModel(models.Model):
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField()
    job = models.ForeignKey("JobModel", on_delete=models.CASCADE)
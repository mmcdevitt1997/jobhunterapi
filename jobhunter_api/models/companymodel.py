from django.db import models
from .jobmodel import JobModel

class CompanyModel (models.Model):
    name = models.CharField(max_length= 50, blank=True)
    should_apply = models.BooleanField(initial=True)
    job = models.ForeignKey("JobModel", on_delete=models.DO_NOTHING)
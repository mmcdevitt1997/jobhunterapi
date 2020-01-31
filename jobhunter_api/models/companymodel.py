from django.db import models
from .jobmodel import JobModel

"""
The model that sets up the data structure for a company.
"""

class CompanyModel (models.Model):
    name = models.CharField(max_length= 50, blank=True)
    should_apply = models.BooleanField(default=True)
    job = models.ForeignKey("JobModel", on_delete=models.DO_NOTHING)
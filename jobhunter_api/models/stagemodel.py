from django.db import models
from .jobmodel import JobModel

"""
This model sets up the data structure for a stage.A stage is created to
track where the user in the job process.
"""

class StageModel(models.Model):
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField()
    job = models.ForeignKey("JobModel", on_delete=models.CASCADE)
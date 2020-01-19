from django.db import models

class JobModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=15, decimal_places=2)
    job_link = models.CharField(max_length=150)
    active = models.BooleanField(initial=True)


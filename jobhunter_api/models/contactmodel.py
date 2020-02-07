from django.db import models
from .companymodel import CompanyModel
from phonenumber_field.modelfields import PhoneNumberField

"""
This model sets up the data structure for a contacts that is related to the
companies that you apply to.
"""

class ContactModel (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    title = models.CharField(max_length=50)
    company = models.ForeignKey("CompanyModel", on_delete=models.CASCADE)
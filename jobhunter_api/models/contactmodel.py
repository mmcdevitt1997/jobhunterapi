from django.db import models
from .companymodel import CompanyModel
from phonenumber_field.modelfields import PhoneNumberField

class ContactModel (models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = phone_number = PhoneNumberField()
    title = models.CharField(max_length = 50)
    company = models.ForeignKey("CompanyModel", on_delete=models.CASCADE)
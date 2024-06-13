# models.py
from django.db import models

class Vendor(models.Model):
    vendor_id = models.CharField(max_length=20, unique=True)
    vendor_fname = models.CharField(max_length=100)
    vendor_lname = models.CharField(max_length=100)
    vendor_email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    vendor_phone_number = models.CharField(max_length=20)
    vendor_company_name = models.CharField(max_length=100)
    vendor_gst_num = models.CharField(max_length=20, blank=True, null=True)
    vendor_company_type = models.CharField(max_length=20)
    vendor_created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.vendor_fname} {self.vendor_lname}"

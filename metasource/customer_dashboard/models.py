from django.db import models
from django.utils import timezone
from datetime import datetime

class Customer(models.Model):
    customer_id = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100)
    country_restrictions = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    delivery_address = models.TextField()
    cutomer_created_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            today = datetime.now().strftime("%y%m%d")
            last_customer = Customer.objects.filter(customer_id__startswith="MSC" + today).order_by('-customer_id').first()
            if last_customer:
                last_serial_number = int(last_customer.customer_id[-3:])
                if last_serial_number < 999:
                    new_serial_number = last_serial_number + 1
                else:
                    new_serial_number = 1000
            else:
                new_serial_number = 1
            self.customer_id = f"MSC{today}{str(new_serial_number).zfill(3)}"
        super().save(*args, **kwargs)

class Material(models.Model):
    material_id = models.CharField(max_length=12, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    firm_budgetary = models.CharField(max_length=20)
    material = models.CharField(max_length=100)
    shape = models.CharField(max_length=100)
    size_in_mm = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    material_need_date = models.DateField()
    remarks = models.TextField()
    material_created_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.material_id:
            today = datetime.now().strftime("%y%m%d")
            last_material = Material.objects.filter(material_id__startswith="MSM" + today).order_by('-material_id').first()
            if last_material:
                last_serial_number = int(last_material.material_id[-3:])
                if last_serial_number < 999:
                    new_serial_number = last_serial_number + 1
                else:
                    new_serial_number = 1000
            else:
                new_serial_number = 1
            self.material_id = f"MSM{today}{str(new_serial_number).zfill(3)}"
        super().save(*args, **kwargs)

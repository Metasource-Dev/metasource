from django.contrib import admin
from .models import Material, Customer

# Register your models here.
admin.site.register(Material),
admin.site.register(Customer)
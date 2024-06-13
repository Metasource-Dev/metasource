from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .models import Vendor
from customer_dashboard.models import Material, Customer
import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class RegisterVendorView(View):
    def get(self, request):
        return render(request, 'vendor/vendor_register.html')

    def post(self, request):
        vendor_fname = request.POST.get('vendor_fname')
        vendor_lname = request.POST.get('vendor_lname')
        vendor_email = request.POST.get('vendor_email')
        vendor_phone_number = request.POST.get('vendor_phone_number')
        vendor_company_name = request.POST.get('vendor_company_name')
        vendor_gst_num = request.POST.get('vendor_gst_num')
        vendor_company_type = request.POST.get('vendor_company_type')
        password = request.POST.get('password')
        
        if vendor_fname and vendor_lname and vendor_email and vendor_phone_number and vendor_company_name and vendor_company_type and password:
            vendor = Vendor.objects.create(
                vendor_fname=vendor_fname,
                vendor_lname=vendor_lname,
                vendor_email=vendor_email,
                vendor_phone_number=vendor_phone_number,
                vendor_company_name=vendor_company_name,
                vendor_gst_num=vendor_gst_num,
                vendor_company_type=vendor_company_type,
                password=password,
                vendor_id=self.generate_vendor_id()
            )
            # self.send_registration_email(vendor)
            return redirect('vendor_registration')  # Redirect to a success page
        else:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('vendor_registration')  # Redirect back to registration page with error message

    def generate_vendor_id(self):
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime("%y%m%d")
        last_vendor_serial_number = self.get_last_vendor_serial_number()
        serial_number = str(last_vendor_serial_number + 1).zfill(3)
        vendor_id = f"MSV{formatted_date}{serial_number}"
        return vendor_id

    def get_last_vendor_serial_number(self):
        last_vendor = Vendor.objects.order_by('-id').first()
        if last_vendor:
            last_serial_number = int(last_vendor.vendor_id[-3:])
            return last_serial_number
        else:
            return 0

    # def send_registration_email(self, vendor):
    #     subject = 'Registration Successful'
    #     message = f"Dear {vendor.vendor_fname},\n\nYour registration with Vendor ID {vendor.vendor_id} is successful.\n\nYour password is: {vendor.password}\n\nThank you."
    #     sender = 'nannapravalika566@gmail.com'  # Your email address
    #     recipient = vendor.vendor_email
    #     send_mail(subject, message, sender, [recipient])

class VendorLoginView(View):
    def get(self, request):
        return render(request, 'vendor/vendor_login.html')

    def post(self, request):
        email = request.POST.get('vendor_email')
        password = request.POST.get('password')
        try:
            vendor = Vendor.objects.get(vendor_email=email, password=password)
            # Check if multiple vendors are found with the same email and password
            if Vendor.objects.filter(vendor_email=email, password=password).count() > 1:
                messages.error(request, 'Multiple vendors found with the same email and password.')
                return redirect('vendor_login')  # Redirect back to login page with error message
            request.session["vendor_id"] = vendor.vendor_id
            messages.success(request, 'Login Successful')
            return redirect('dashboard')
        except Vendor.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return redirect('vendor_login')  # Redirect back to login page with error message

# @method_decorator(login_required, name='dispatch')
class DashboardView(View):
    # @method_decorator(login_required)
    def get(self, request):
        vendor_id = request.session["vendor_id"]
        return render(request, 'vendor/dashboard.html', {"vendor_id": vendor_id})

# @method_decorator(login_required, name='dispatch')
class QuotationsView(View):
    # @method_decorator(login_required)
    def get(self, request): 
        basic_list = Customer.objects.all()
        materials = Material.objects.all()
        vendor_id = request.session.get('vendor_id')
        return render(request, 'vendor/vendor_rfq.html', {"vendor_id": vendor_id, "materials": materials, "basic_list": basic_list})
    
# @method_decorator(login_required, name='dispatch')
class InventoryView(View):
    # @method_decorator(login_required)
    def get(self,request):
        vendor_id = request.session["vendor_id"]
        return render(request, "vendor/vendor_inventory.html")

# @method_decorator(login_required, name='dispatch')
class OrdersView(View):
    # @method_decorator(login_required)
    def get(self,request):
        vendor_id = request.session["vendor_id"]
        return render(request, "vendor/vendor_po.html")
    
# @method_decorator(login_required, name='dispatch')
class BidView(View):
    # @method_decorator(login_required)
    def get(self,request):
        vendor_id = request.session["vendor_id"]
        return render(request, "vendor/vendor_rfq_bid.html")



from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from vendor_dashboard.models import Vendor
from customer_dashboard.models import Material, Customer
import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CutomerAddFormView(View):
    def get(self, request):
        basic_list = Customer.objects.all()
        materials = Material.objects.all()
        customer_id = request.session.get('customer_id')
        return render(request, 'customer/customer_add_enquiry.html',{"customer_id": customer_id, "materials": materials, "basic_list": basic_list})  

    def post(self, request):
        # Get form data from POST request
        email = request.POST.get('email')
        company_name = request.POST.get('company_name')
        country_restrictions = request.POST.get('country_restrictions')
        phone_no = request.POST.get('phone_no')
        delivery_address = request.POST.get('delivery_address')

        firm_budgetary = request.POST.get('firm_budgetary_1')
        material = request.POST.get('material_1')
        shape = request.POST.get('shape_1')
        size_in_mm = request.POST.get('size_in_mm_1')
        quantity = request.POST.get('quantity_1')
        material_need_date = request.POST.get('material_need_date_1')
        remarks = request.POST.get('remarks_1')

        # Create Customer instance
        customer = Customer.objects.create(
            email=email,
            company_name=company_name,
            country_restrictions=country_restrictions,
            phone_no=phone_no,
            delivery_address=delivery_address
        )

        # Create Material instance associated with the Customer
        material = Material.objects.create(
            customer=customer,
            firm_budgetary=firm_budgetary,
            material=material,
            shape=shape,
            size_in_mm=size_in_mm,
            quantity=quantity,
            material_need_date=material_need_date,
            remarks=remarks
        )

        # html_content = "<br/><p>HI <strong>"+ str(Customer.company_name)+" <strong> your RFQ has been submitted "
        # from_mail = DEFAULT_FROM_EMAIL
        # to_mail = [object.email]
        # # if send_mail(subject,message,from_mail,to_mail):
        # msg = EmailMultiAlternatives("INTERNSHIP POST Status", html_content, from_mail, to_mail)
        # msg.attach_alternative(html_content, "text/html")
        # if msg.send():
        #     print("Sent")
        return redirect('customer_enquiries')  # Replace 'success_url' with the URL name for the success page

    
    
class CustomerLoginView(View):
    def get(self, request):
        return render(request, 'customer/customer_login.html')  # Replace 'customer_login.html' with the actual template name

    def post(self, request):
        email = request.POST.get('email')
        customer_id = request.POST.get('password')

        try:
            customer = Customer.objects.get(email=email, customer_id=customer_id)
            # Set session variables or perform any necessary authentication
            request.session['customer_id'] = customer.customer_id  # Set customer ID in session
            messages.success(request, 'Login Successful')
            return redirect('customer_dashboard')  # Redirect to customer dashboard
        except Customer.DoesNotExist:
            messages.error(request, 'Invalid email or customer ID.')
            return redirect('customer_dashboard')  # Redirect back to login page with error message


class AddFormView(View):
    def get(self, request):
        return render(request, 'customer/material_form.html')  # Replace 'your_template.html' with the actual template name

    def post(self, request):
        # Get form data from POST request
        email = request.POST.get('email')
        company_name = request.POST.get('company_name')
        country_restrictions = request.POST.get('country_restrictions')
        phone_no = request.POST.get('phone_no')
        delivery_address = request.POST.get('delivery_address')

        firm_budgetary = request.POST.get('firm_budgetary_1')
        material = request.POST.get('material_1')
        shape = request.POST.get('shape_1')
        size_in_mm = request.POST.get('size_in_mm_1')
        quantity = request.POST.get('quantity_1')
        material_need_date = request.POST.get('material_need_date_1')
        remarks = request.POST.get('remarks_1')

        # Create Customer instance
        customer = Customer.objects.create(
            email=email,
            company_name=company_name,
            country_restrictions=country_restrictions,
            phone_no=phone_no,
            delivery_address=delivery_address
        )

        # Create Material instance associated with the Customer
        material = Material.objects.create(
            customer=customer,
            firm_budgetary=firm_budgetary,
            material=material,
            shape=shape,
            size_in_mm=size_in_mm,
            quantity=quantity,
            material_need_date=material_need_date,
            remarks=remarks
        )

        # html_content = "<br/><p>HI <strong>"+ str(Customer.company_name)+" <strong> your RFQ has been submitted "
        # from_mail = DEFAULT_FROM_EMAIL
        # to_mail = [object.email]
        # # if send_mail(subject,message,from_mail,to_mail):
        # msg = EmailMultiAlternatives("INTERNSHIP POST Status", html_content, from_mail, to_mail)
        # msg.attach_alternative(html_content, "text/html")
        # if msg.send():
        #     print("Sent")
        return redirect('customer_login')  # Replace 'success_url' with the URL name for the success page
    
class CustomerDashboardView(View):
      
    def get(self, request):
        
        return render(request, 'customer/customer_dashboard.html' )

class CustomerEnquiriesView(View):
      
    def get(self, request): 
        basic_list = Customer.objects.all()
        materials = Material.objects.all()
        customer_id = request.session.get('customer_id')
        return render(request, 'customer/customer_enquiries.html', {"customer_id": customer_id, "materials": materials, "basic_list": basic_list})

class CustomerOrderView(View):
      
    def get(self, request):
        
        return render(request, 'customer/customer_orders.html' )

class CustomerQuotationsView(View):
      
    def get(self, request): 
         
        return render(request, 'customer/customer_quotations.html')
    

class CustomerReceivedOrdersView(View):
      
    def get(self, request):
        
        return render(request, 'customer/customer_received_orders.html' )
    

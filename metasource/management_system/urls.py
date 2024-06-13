"""
URL configuration for management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from vendor_dashboard.views import *
from customer_dashboard.views import *
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='home'),
    path('add-form/', AddFormView.as_view(), name='add_form'),
    path('vendor-register/', RegisterVendorView.as_view(), name='vendor_registration'),
    path('vendor-login/', VendorLoginView.as_view(), name='vendor_login'),
    path('vendor-dashboard/', DashboardView.as_view(), name='dashboard'),
    path('vendor-quotations/', QuotationsView.as_view(), name='quotations'),
    path('vendor-orders/', OrdersView.as_view(), name='orders'),
    path('vendor-inventory/', InventoryView.as_view(), name='inventory'),
    path('vendor-rfq-bids/', BidView.as_view(), name='rfq_bids'),
    path('customer-login/', CustomerLoginView.as_view(), name='customer_login'),
    path('customer-dashboard/', CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('customer-enquiries/', CustomerEnquiriesView.as_view(), name='customer_enquiries'),
    path('customer-orders/', CustomerOrderView.as_view(), name='customer_orders'),
    path('customer-quotations/', CustomerReceivedOrdersView.as_view(), name='customer_quotations'),
    path('customer-received-orders/', CustomerQuotationsView.as_view(), name='customer_received_orders'),
    path('customer-add-form/', CutomerAddFormView.as_view(), name='customer_add_form'),

]

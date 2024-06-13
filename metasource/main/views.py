from django.shortcuts import render, redirect
from django.views import View 
from django.contrib import messages 
from django.core.mail import EmailMultiAlternatives
from management_system.settings import DEFAULT_FROM_EMAIL
import email
 

# Create your views here.
 
class MainView(View):
    
    def get(self, request):
         
        return render(request, 'index.html')
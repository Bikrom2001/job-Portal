from django.shortcuts import render
from jobportal.models import *
from jobportal.forms import *

def register_view(request):
    
    form_data = RegisterForm()
    
    context ={
        'form_data':form_data,
        'title':"Register Page",
        'form_title': 'User Registration Form',
        'form_btn': 'Register',
    }
    
    return render(request, 'master/base-form.html', context)
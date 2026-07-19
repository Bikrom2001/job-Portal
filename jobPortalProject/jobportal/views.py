from django.shortcuts import render

def register_view(request):
    
    context ={
        'title':"Register Page",
        'form_title': 'User Registration Form',
        'form_btn': 'Register',
    }
    
    return render(request, 'master/base-form.html', context)
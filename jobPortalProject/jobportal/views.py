from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from jobportal.models import *
from jobportal.forms import *
from django.contrib import messages

def register_view(request):
    
    if request.method == 'POST':
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'User Creation Successfully.')
            return redirect('login_view')
        
    
    form_data = RegisterForm()
    
    context ={
        'form_data':form_data,
        'title':"Register Page",
        'form_title': 'User Registration Form',
        'form_btn': 'Register',
    }
    
    return render(request, 'master/base-form.html', context)


def login_view(request):
    
    if request.method == "POST":
        form_data = AuthenticationForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            if user:
                login(request, user)
                messages.success(request, 'User Login Successfully.')
                return redirect('dashboard_view')
            
        messages.error(request, 'Invalid Credentials.')
    
    form_data = AuthenticationForm()
    
    context ={
        'form_data':form_data,
        'title':"Login Page",
        'form_title': 'User Login Form',
        'form_btn': 'Login',
    }
    
    return render(request, 'master/base-form.html', context)

@login_required
def dashboard_view(request):
    
    return render(request, 'dashboard.html')


@login_required
def logout_view(request):
    
    logout(request)
    
    return redirect('login_view')



def profile_view(request):
    
    return render(request, 'profile.html')


@login_required
def update_profile_view(request):
    current_user = request.user
    if current_user.user_type == 'Recruiter':
        try:
            profile_data = RecruiterProfileModel.objects.get(recruiter= current_user)
        except:
            profile_data = None
        if request.method == 'POST':
            form_data = RecruiterProfileUpdateForm(request.POST, request.FILES, instance=profile_data)
            if form_data.is_valid():
                data = form_data.save(commit=False)
                data.recruiter = current_user
                data.save()
                messages.success(request, 'Profile Updated Successfully.')
                return redirect('profile_view')
        form_data = RecruiterProfileUpdateForm(instance=profile_data)
    else:
        try:
            profile_data = SeekerProfileModel.objects.get(seeker = current_user)
        except:
            profile_data = None
        if request.method == 'POST':
            form_data = SeekerProfileUpdateForm(request.POST, request.FILES, instance=profile_data)
            if form_data.is_valid():
                data = form_data.save(commit=False)
                data.seeker = current_user
                data.save()
                messages.success(request, 'Profile Updated Successfully.')
                return redirect('profile_view')
        form_data = SeekerProfileUpdateForm(instance=profile_data)

    context = {
        'form_data': form_data,
        'title': 'Update Profile Info Page',
        'form_title': 'Update Profile Info Form',
        'form_btn': 'Update Profile',
    }
    return render(request, 'master/base-form.html', context)
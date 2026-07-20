from django.urls import path
from jobportal.views import *


urlpatterns = [
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    
    
    path('', dashboard_view, name='dashboard_view'),
    path('profile-view/', profile_view, name='profile_view'),
    path('update-profile-view/', update_profile_view, name='update_profile_view'),
    
    
    path('browse-job/',browse_job_view, name='browse_job_view'),
    path('post-job/',post_job_view,name='post_job_view'),
]




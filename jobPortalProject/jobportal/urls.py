from django.urls import path
from jobportal.views import *


urlpatterns = [
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
]

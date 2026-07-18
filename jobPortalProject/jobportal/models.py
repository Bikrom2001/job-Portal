from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    USER_TYPES = [
        ('Recruiter', 'Recruiter'),
        ('Seeker', 'Seeker'),
    ]
    
    display_name = models.CharField(max_length=200, null=True)
    user_type = models.CharField(choices=USER_TYPES, max_length=20, null=True)
    
    def __str__(self):
      return f'{self.username} - {self.user_type}'


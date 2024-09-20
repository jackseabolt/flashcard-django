from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin): 
    """Database model for users in the system"""

    email =  models.EmailField(max_legnth=255, unique=True)
    name = models.CharField(max_length=266)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME = 'email' # this override the default setting of using username
    REQUIRED_FIELDS = ['name']

    def get_full_name(self): 
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self): 
        """Retrieve short name of user"""
        return self.name
    
    def __str__(self): 
        """Return string representation of user"""
        return self.email
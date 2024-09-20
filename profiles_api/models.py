from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager): 
    """Manager for user profiles"""

    def create_user(self, email, name, password=None): 
        """Create a new user profile"""
        if not email: 
            raise ValueError('User must have an email address')
        
        # the first half of email are case-sensitive, the second half 
        # is case-insensitive. Best practice to enforce this
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password) # this encrypts the password
        user.save(using=self._db) # django can support multiple databases

        return user 

    def create_super_user(self, email, name, password): 
        """Create new superuser with provided details"""
        user = self.create_user(email, name, password)
        
        # this is not defined in UserProfile, automatically added be PermissionsMixin
        user.is_superuser = True 
        user.is_staff = True

        user.save(using=self._db); # django can support multiple databases


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

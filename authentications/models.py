from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import pre_save,post_save ,post_delete

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
      
class User(AbstractUser):
  username= None
  is_person = models.BooleanField(default=False)
  is_company = models.BooleanField(default=False)
  email=models.EmailField("email_address", unique=True)
  phone_number = models.CharField(max_length=11)
  address = models.CharField(max_length=100)
  image = models.ImageField( null= False)
  tax_number = models.CharField(max_length=100,null=True,blank=True)
  objects = UserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  

    

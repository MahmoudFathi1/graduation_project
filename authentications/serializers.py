from django.db import models
from rest_framework import serializers ,permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate , login
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[ 'email', 'is_person']

            
class CompanyCustomRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['email','password', 'password2','first_name','address','phone_number','tax_number']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            address=self.validated_data['address'],
            phone_number=self.validated_data['phone_number'],
            # image=self.validated_data['image'],
            tax_number=self.validated_data['tax_number']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_company=True
        user.save()
        return user
    
    
class PersonCustomRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    
    class Meta:
        model=User
        fields=['email','password', 'password2','first_name','address','phone_number']
        extra_kwargs={
            'password':{'write_only':True}
        }
    

    def save(self, **kwargs):
        user=User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            address=self.validated_data['address'],
            phone_number=self.validated_data['phone_number'],
            # image=self.validated_data['image']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_person=True
        user.save()
        return user



class LoginSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 
    class Meta:
        
        model= User
        fields = ('email','password')
        # read_only_fields = ['token']
        


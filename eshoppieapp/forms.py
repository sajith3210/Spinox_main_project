
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class indexform(forms.ModelForm):
    class Meta:
        model=AdminTable
        fields=("username","password")
        labels={
            'username':'Enter username',
            'password':'password',
        }
        widgets={
            'password':forms.PasswordInput(),
        }
class catform(forms.ModelForm):
    class Meta:
        model=category_details
        fields="__all__"

class sellerform(forms.ModelForm):
    class Meta:
        model=SellerTable
        fields=('sellername', 'adress', 'email','password','phone_number',)
        labels={
            'sellername':'sellername','adress':'Adress','email':'Email','password':'password', 'phone_number':'phone'
        }
        widgets={
            'adress':forms.Textarea(attrs={'rows':8,'cols':18}),
            'email':forms.EmailInput(),
            'password':forms.PasswordInput(),
        }
class productform(forms.ModelForm):
    class Meta:
        model=ProductTable
        fields=("__all__")
        labels={
            'category_ID':'Category','Seller_ID':'seller'
        }
class userform(forms.ModelForm):
    class Meta:
        model=user
        fields="__all__"

        widgets={
             'email':forms.EmailInput(),
            'password':forms.PasswordInput(),
            'confirm_password':forms.PasswordInput(),
            'adress':forms.Textarea(attrs={'rows':8,'cols':18}),
            
        }
'''class createuserform(UserCreationForm):
    class Meta:
        model=user
        #fields=['Username','email','password1','password2']'''

class registerform(forms.ModelForm):
    class Meta:
        model=user
        fields="__all__" 
        widgets={
            'email':forms.EmailInput(),
            'password':forms.PasswordInput(),
           
            'adress':forms.Textarea(attrs={'rows':8,'cols':18}),
            
        }

        def clean(self):
            cleaned_data=super().clean()
            valpwd=self.cleaned_data['password']
            valrpwd=self.cleaned_data['confirm_password']
            if valpwd !=valrpwd:
                raise forms.ValidationError("Password does not match")
class loginform(forms.ModelForm):
    class Meta:
        model=user
        fields=('username','password')
        widgets={
            'password':forms.PasswordInput(),
        }
class buyprodform(forms.ModelForm):
    class Meta:
        model=ProductTable
        fields=('category_ID',)
        labels={
            'category_ID':'Category',
        }
class cartform(forms.ModelForm):
    class Meta:
        models=cart
        fields="__all__"

class orderform(forms.ModelForm):
    class Meta:
        model=orders
        exclude=('user_ID','Product_ID')
      
        
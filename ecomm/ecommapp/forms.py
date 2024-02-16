from django import forms
from django.contrib.auth.models import User
from ecommapp.models import Carts,Orders



class UserRegister(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        #widget used for styling the form
    widgets={
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Firstname'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname'}),
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),

    }
class UserLogin(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'password'})
        }
class CartForm(forms.ModelForm):
    class Meta:
        model=Carts
        fields=['quantity']
        widgets={
            'quantity':forms.NumberInput(attrs={'class':'form-control'})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['address','email']
        widgets={
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
from django import forms
import re

from .models import Manager

class RegForm(forms.Form):
    first_name=forms.CharField(label="enter fname",max_length=100,widget=forms.TextInput(attrs={"placeholder":"firstName","class":"form-control"}))
    last_name=forms.CharField(label="enter sname",max_length=100,widget=forms.TextInput(attrs={"placeholder":"secondNmae","class":"form-control"}))
    email=forms.EmailField(label="enter email",widget=forms.EmailInput(attrs={'placeholder':"email","class":"form-control"}))
    password=forms.CharField(label="enter password",widget=forms.TextInput(attrs={'placeholder':"password","class":"form-control"}))
    age=forms.IntegerField(label="enter age",widget=forms.TextInput(attrs={'placeholder':"age","class":"form-control"}))
    def clean(self):
        pswd=self.cleaned_data.get("password")
        if len(pswd)>8:
            msg="password is more than 8 characters"
            
            self.add_error("password",msg)
        return super().clean()
class login(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100 ,widget=forms.PasswordInput(attrs={"placeholder":"password"}))
    def clean(self):
        pass1=self.cleaned_data.get("password")
        if not re.findall('[0-9]',pass1):
            msg1="login faild "
            self.add_error("password",msg1)
        return super().clean()


class ManagermodelForm(forms.ModelForm):
    class Meta:
        model=Manager
        fields="__all__"
        widget={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "qualifiaction":forms.TextInput(attrs={"class":"form-control"}),
        }
    


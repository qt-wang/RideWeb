from django import forms
from .models import ride, driver
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']  
        
class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = driver
        fields = ['carType', 'plateNum', 'capa']  
        
class rideCreationForm(forms.ModelForm):
    class Meta:
        model = ride
        fields = ['startTime', 'area', 'destination', 'passengerNum', 'shareable']
        labels = {
          "startTime":"StartTime (valid format: MM/DD/YYYY HH:MM)",
          "area":"Destination Area",
          "shareable":"Check this box if you want to share this ride",
          "passengerNum": "Number of passengers from your party",
        }
        
class startTimeEditForm(forms.ModelForm):
    class Meta:
        model = ride
        fields = ['startTime']
        labels = {
          "startTime":"StartTime (valid format: MM/DD/YYYY HH:MM)",
        }
        
class areaEditForm(forms.ModelForm):
    class Meta:
        model = ride
        fields = [ 'area']
        labels = {
          "area":"Destination Area",
        }
        
class destinationEditForm(forms.ModelForm):
    class Meta:
        model = ride
        fields = [ 'destination']
        labels = {
          "destination":"Destination",
        }
        
class passengerNumEditForm(forms.ModelForm):
    class Meta:
        model = ride
        fields = ['passengerNum']
        labels = {
          "passengerNum": "Number of passengers from your party",
        }
        
class shareableEditForm(forms.ModelForm):
    class Meta:
        model = ride
        fields = ['shareable']
        labels = {
          "shareable":"Check this box if you want to share this ride",
        }
        
class driverRegisterForm(forms.ModelForm):
    class Meta:
        model = driver
        fields = [ 'carType', 'plateNum', 'capa']        

class search_share_Form(forms.ModelForm):
    latestStartTime  = forms.DateTimeField()
    class Meta:
        model = ride
        fields = ['startTime', 'latestStartTime','area', 'passengerNum']
        labels = {
          "startTime":"StartTime (valid format: MM/DD/YYYY HH:MM)",
          "latestStartTime":"LatestStartTime (valid format: MM/DD/YYYY HH:MM)",
          "area":"Destination Area",
          "passengerNum": "Number of passengers from your party",
        }
        
class search_unconfirmed_Form(forms.ModelForm):
    latestStartTime  = forms.DateTimeField()
    class Meta:
        model = ride
        fields = ['startTime', 'latestStartTime','area']
        labels = {
          "startTime":"StartTime (valid format: MM/DD/YYYY HH:MM)",
          "latestStartTime":"LatestStartTime (valid format: MM/DD/YYYY HH:MM)",
          "area":"Destination Area",
        }
        
        
        

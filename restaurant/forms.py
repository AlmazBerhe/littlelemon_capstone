from django import forms
from .models import Booking
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'reservation_slot': forms.Select(choices=[])
        }
        
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["username", "password"]
from django import forms  
from .models import Tracker,Driver,Chat

class TrackerForm(forms.ModelForm):  
    class Meta:  
        model = Tracker  
        fields = "__all__"  


class DriverForm(forms.ModelForm):  
    class Meta:  
        model = Driver  
        fields = "__all__" 

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat 
        fields = "__all__" 
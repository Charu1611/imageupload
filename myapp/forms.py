from django.db import models  
from django.forms import fields  
# from .models import UploadImage  
from django import forms  
from .models import UploadImage

class UploadImageForm(forms.ModelForm):
    class Meta:
        model=UploadImage
        fields=("caption","image")


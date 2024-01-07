from django import forms
from django.db import models
from .models import SchemaCertificativo, Auditor

class SchemaForm(forms.Form):
    schema_certificazione = models.CharField(max_length=300, unique=True) 

class SchemaCertificativoForm(forms.ModelForm):
    class Meta:
        model = SchemaCertificativo
        fields = '__all__'  # Include all fields from the model

class AuditorForm(forms.ModelForm):
    class Meta:
        model = Auditor
        fields = '__all__'  # Include all fields from the model
    

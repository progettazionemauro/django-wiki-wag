from django.contrib import admin

# Register your models here.
from django.forms.widgets import TextInput
from django import forms
from .models import *



@admin.register(SchemaCertificativo)
class SchemaCertificativoAdmin(admin.ModelAdmin):
    pass

@admin.register(Auditor)                # registrazione in admin del widget per l'inseimento del n° telefonico
class AuditorAdmin(admin.ModelAdmin):
    # list_display=["nome_auditor", "email_auditor", "cellulare_auditor", "Link_schema_certificativo", "disponibile"]
    # list_editable=('disponibile',)
    # form = PhoneForm
    
    def Link_schema_certificativo(self, obj):
       # return format_html('<a  href="https://127.0.0.1:8000/product/{0}" >{1}</a>',obj.id, obj.email_auditor) #url con parametri
        return format_html('<a  href="https://en.wikipedia.org/wiki/Nigeria" >{1}</a>',obj.id, obj.email_auditor)
    
    @admin.register(FixedTableContent)
    class FixedTableContentAdmin(admin.ModelAdmin):    list_display = ('nation', 'capital')

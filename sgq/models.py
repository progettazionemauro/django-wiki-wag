from django.db import models

# from phonenumber_field.modelfields import PhoneNumberField
# from location_field.models.plain import PlainLocationField

""" class Place(models.Model):  
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7) """



""" class SampleModel(models.Model):
    address = AddressField(max_length=100)
    geolocation = GeoLocationField(blank=True)

    def __str__(self):
        return self.address """

class SchemaCertificativo(models.Model): #registrato
    
    schema_certificazione = models.CharField(max_length=300, unique=True) 
    class Meta:
        verbose_name_plural="Schema Certificativo"

    def __str__(self):
        return self.schema_certificazione

class Auditor(models.Model): #registration
    
    nome_auditor = models.CharField(max_length=300, unique=True) # fare attenzione: nel momento in cui si sostituisce il database è necessario inserire o il valore di default oppure blank and null: vedere qui stackoverflow: https://stackoverflow.com/a/73509787/11233866       
    email_auditor=models.EmailField(max_length=254)
    # cellulare_auditor=PhoneNumberField()
    schema_certificativo=models.ManyToManyField(SchemaCertificativo)
    disponibile = models.BooleanField(default=True)
    foto = models.FileField(blank=True, default="default.jpg")
    
    class Meta:
        verbose_name = 'Auditor'
        verbose_name_plural = 'Auditor'

    def __str__(self):
        return f"{self.nome_auditor}"
    
# the model to pass to wagtail 
class FixedTableContent(models.Model):
    nation = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)

    def __str__(self):
        return self.nation
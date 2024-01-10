
from django.contrib import admin
from django.urls import path, include
from wagtail import urls as wagtail_urls

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('wagtail/', include('wagtail.core.urls')), # nuovo inserimento
    path('wagtail-admin/', include(wagtail_urls)), # nuovo inserimento
   
]

from django.contrib import admin
from django.urls import path, include
from wagtail import urls as wagtail_urls

urlpatterns = [
    path('', include('sgq.urls')),  # Include the app-level URLs
    path('admin/', admin.site.urls),
    path('wagtail/', include('wagtail_urls')), # nuovo inserimento
    path('wagtail-admin/', include(wagtail_urls)), # nuovo inserimento
   
]
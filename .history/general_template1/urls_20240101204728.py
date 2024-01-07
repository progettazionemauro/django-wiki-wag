from wagtail import urls as wagtail_urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('sgq.urls')),  # Include the app-level URLs
    path('admin/', admin.site.urls),
    # path('wagtail/', include('wagtail.core.urls')), # nuovo inserimento
    path('wagtail/', include('wagtail_urls')), # nuovo inserimento
   
]
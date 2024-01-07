from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('sgq.urls')),  # Include the app-level URLs
    path('admin/', admin.site.urls),
   
]
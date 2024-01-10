from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    path('', include('sgq.urls')),  # Include the app-level URLs
    path('admin/', admin.site.urls),
    path('wagtail-admin/', include(wagtailadmin_urls)),  # Include Wagtail admin URLs
    path('wagtail/', include(wagtail_urls)),  # Include Wagtail core URLs
]
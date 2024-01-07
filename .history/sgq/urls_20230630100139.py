from django.urls import path
from .views import (home_page,
                    SchemaCertificativoListView, 
                    SchemaCertificativoDetailView, 
                    AuditorListView,
                    
)
from .views import create_schema_certificativo, update_schema_certificativo, delete_schema_certificativo


app_name = 'sgq'  # Add this line to set the app namespace

urlpatterns = [
    path('', home_page, name='home_page'),
    path('schema_certificativo/', SchemaCertificativoListView.as_view(), name='schema_certificativo_list'),
    path('schema_certificativo/<int:pk>/', SchemaCertificativoDetailView.as_view(), name='schema_certificativo_detail'),
    path('auditor_list/', AuditorListView.as_view(), name='auditor_list'),
    path('schema_certificativo/create/', create_schema_certificativo, name='create_schema_certificativo'),
    path('schema_certificativo/update/<int:pk>/', update_schema_certificativo, name='update_schema_certificativo'),
    path('schema_certificativo/delete/<int:pk>/', delete_schema_certificativo, name='delete_schema_certificativo'),
    
]

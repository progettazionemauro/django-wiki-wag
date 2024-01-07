from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import SchemaCertificativo, Auditor
from .forms import SchemaCertificativoForm, AuditorForm

def home_page(request):
    return render(request, 'home.html')

class SchemaCertificativoListView(ListView):
    model = SchemaCertificativo
    template_name = 'schema_certificativo_list.html'

class SchemaCertificativoDetailView(DetailView):
    model = SchemaCertificativo
    template_name = 'schema_certificativo_detail.html'
    
class AuditorListView(ListView):
    model=Auditor
    template_name='auditor_list.html'

# Views for forms
def create_schema_certificativo(request):
    if request.method == 'POST':
        form = SchemaCertificativoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schema_certificativo_list')
    else:
        form = SchemaCertificativoForm()
    return render(request, 'create_schema_certificativo.html', {'form': form})

def update_schema_certificativo(request, pk):
    schema_certificativo = SchemaCertificativo.objects.get(pk=pk)
    if request.method == 'POST':
        form = SchemaCertificativoForm(request.POST, instance=schema_certificativo)
        if form.is_valid():
            form.save()
            return redirect('schema_certificativo_list')
    else:
        form = SchemaCertificativoForm(instance=schema_certificativo)
    return render(request, 'update_schema_certificativo.html', {'form': form, 'pk': pk})

def delete_schema_certificativo(request, pk):
    schema_certificativo = SchemaCertificativo.objects.get(pk=pk)
    if request.method == 'POST':
        schema_certificativo.delete()
        return redirect('schema_certificativo_list')
    return render(request, 'delete_schema_certificativo.html', {'schema_certificativo': schema_certificativo})

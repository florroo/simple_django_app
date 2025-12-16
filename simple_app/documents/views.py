from django.shortcuts import render
from .models import Document
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/users/login/')
def documents_list(request):
    documents = Document.objects.all().order_by('-date') # - in descending order
    return render(request, 'documents/documents_list.html', { 'documents': documents })

@login_required(login_url='/users/login/')
def document_page(request, slug):
    document = Document.objects.get(slug=slug)
    return render(request, 'documents/document_page.html', { 'document': document })

@login_required(login_url='/users/login/')
def document_new(request):
    return render(request, 'documents/document_new.html')
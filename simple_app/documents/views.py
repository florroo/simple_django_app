from django.shortcuts import render
from .models import Document
from django.http import HttpResponse

# Create your views here.
def documents_list(request):
    documents = Document.objects.all().order_by('-date') # - in descending order
    return render(request, 'documents/documents_list.html', { 'documents': documents })

def document_page(request, slug):
    document = Document.objects.get(slug=slug)
    return render(request, 'documents/document_page.html', { 'document': document })
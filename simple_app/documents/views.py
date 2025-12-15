from django.shortcuts import render
from .models import Document

# Create your views here.
def documents_list(request):
    documents = Document.objects.all().order_by('-date') # - in descending order
    return render(request, 'documents/documents_list.html', { 'documents': documents })
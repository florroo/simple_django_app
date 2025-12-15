from django.shortcuts import render

# Create your views here.
def documents_list(request):
    return render(request, 'documents/documents_list.html')
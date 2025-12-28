from django.shortcuts import render, redirect
from .models import Document
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from .forms import DocumentForm

# Create your views here.
@login_required(login_url='/users/login/')
def documents_list(request):
    documents = Document.objects.filter(owner=request.user).order_by('-date') # - in descending order
    return render(request, 'documents/documents_list.html', { 'documents': documents })


@login_required(login_url='/users/login/')
def document_page(request, slug):
    document = get_object_or_404(Document, slug=slug, owner=request.user)
    return render(request, 'documents/document_page.html', { 'document': document })


@login_required(login_url='/users/login/')
def document_new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')

        if not title or not file:
            return HttpResponse("title and file are required", status=400)

        document = Document.objects.create(
            owner = request.user,
            title = title,
            description = description,
            file = file,
            slug = slugify(title)
        )

        return redirect('documents:list')

    return render(request, 'documents/document_new.html')


@login_required(login_url='/users/login/')
def document_edit(request, slug):
    document = get_object_or_404(Document, slug=slug, owner=request.user)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('documents:page', slug=document.slug)
    else:
        form = DocumentForm(instance=document)

    return render(request, 'documents/document_edit.html', {'form': form, 'document': document})


@login_required(login_url="/users/login/")
def  document_delete(request, slug):
    document = get_object_or_404(Document, slug=slug, owner=request.user)

    if request.method == "POST":
        document.delete()
        return redirect("documents:list")

    return render(request, "documents/document_confirm_delete.html", {"document": document})
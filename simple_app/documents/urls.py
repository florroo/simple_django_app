from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.documents_list, name="list"),
    path('<slug:slug>', views.document_page, name="page"),
]

from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.documents_list, name="list"),
    path('new-document/', views.document_new, name="new-document"),
    path('<slug:slug>', views.document_page, name="page"),
]

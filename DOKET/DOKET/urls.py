"""DOKET URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('invoices/',include('invoice_manager.urls')),
    path('admin/', admin.site.urls)

]

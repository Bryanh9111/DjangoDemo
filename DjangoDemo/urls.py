# Databricks notebook source
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redirect root URL to the first report
    path('', lambda request: redirect('report_view', report_name='Oracle GL Vs OBS'), name='home'),
    
    # Include the frontend app's URLs
    path('report/', include('frontend.urls')), 
]

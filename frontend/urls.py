# Databricks notebook source
from django.urls import path
from . import views

urlpatterns = [
    path('data-table/', views.data_table_view, name='data_table'),
]

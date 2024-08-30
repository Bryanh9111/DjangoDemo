# Databricks notebook source
import requests
from django.shortcuts import render

def data_table_view(request):
    # Fetch data from the data table API
    response = requests.get('http://localhost:5001/updated-data/process')
    data = response.json()

    # Fetch user info from the user info API
    user_response = requests.get('http://127.0.0.1:5002/user-info')
    user_info = user_response.json()

    # Pass both the data and user info to the template
    context = {
        'data': data,
        'user_info': user_info,
    }
    return render(request, 'frontend/data_table.html', context)

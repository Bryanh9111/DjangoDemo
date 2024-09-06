# Databricks notebook source
import requests
from django.shortcuts import render
from requests.exceptions import RequestException

def fetch_report_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError if the response was unsuccessful
        return response.json()
    except RequestException:
        # In case of a failure (connection refused, timeout, etc.), return an empty dataset
        return []

def report_view(request, report_name):  # Updated to match 'report_name'
    # Define the URLs for each report
    report_urls = {
        'Oracle GL Vs OBS': 'http://localhost:5001/updated-data/process',
        'OBS Actual Vs Flash': 'http://localhost:5003/getreport',
        'B2B Trade Reconciliation': 'http://localhost:5004/getreport'
    }

    # Get the API URL for the selected report
    api_url = report_urls.get(report_name, '')
    
    # Fetch data from the API or return an empty dataset on failure
    data = fetch_report_data(api_url)

    # Fetch user info (assuming this API is always available)
    user_info = requests.get('http://127.0.0.1:5002/user-info').json()

    # Prepare the context with user info and report data
    context = {
        'report_name': report_name,  # Make sure this is consistent
        'data': data,  # The dataset (either from the API or empty if the request failed)
        'user_info': user_info
    }

    return render(request, 'frontend/report_page.html', context)

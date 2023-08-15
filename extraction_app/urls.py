from django.contrib import admin
from django.urls import path
from extraction_app import views
#text_report_training

urlpatterns = [
    path('extract_text', views.extract_text, name="extract_text"),
]

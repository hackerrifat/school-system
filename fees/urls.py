from django.urls import path
from .views import fee_report

urlpatterns = [
    path('report/', fee_report, name='fee_report'),
]
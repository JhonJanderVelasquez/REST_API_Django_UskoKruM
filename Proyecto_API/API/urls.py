from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyView.as_view(), name="companies_list"),
]
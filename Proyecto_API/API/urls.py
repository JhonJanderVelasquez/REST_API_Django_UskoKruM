from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyView.as_view(), name="companies_list"),
    path('companies/<int:id>', views.CompanyView.as_view(), name='companies_process'),
]
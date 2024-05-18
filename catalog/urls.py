from django.urls import path

from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/', views.CatalogTemplateView.as_view(), name='catalog'),
    path('catalog/<slug:cats_id>/', views.CatalogCompaniesListView.as_view(), name='companies'),
    path('product/<slug:product_id>/', views.ProductDetailView.as_view(), name='product'),
]

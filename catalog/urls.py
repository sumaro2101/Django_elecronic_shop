from django.urls import path

from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/', views.CatalogTemplateView.as_view(), name='catalog'),
    path('catalog/<slug:cats_id>/', views.CatalogCompaniesListView.as_view(), name='companies'),
    path('product/create/', views.ProductCreateView.as_view(), name='create'),
    path('product/update/<slug:product_id>/', views.ProductUpdateView.as_view(), name='update'),
    path('product/delete/<slug:product_id>/', views.ProductDeleteView.as_view(), name='delete'),
    path('product/<slug:product_id>/', views.ProductDetailView.as_view(), name='product'),
]

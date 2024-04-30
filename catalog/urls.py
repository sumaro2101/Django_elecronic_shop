from django.urls import path
from . import views


urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:cats_id>/', views.catalog_companies, name='companies'),
    path('product/<slug:product_id>/', views.product, name='product'),
]

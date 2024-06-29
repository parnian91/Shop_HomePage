from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.Store_view, name = 'store_items'),
    path('product/<int:pk>', views.Product_view, name = 'product_items'),
]
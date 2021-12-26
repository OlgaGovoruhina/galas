from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index),

    path('categories/', views.categories_list),
    path('categories/<int:category_id>/', views.products_list),
    path('products/<int:product_id>/', views.product_details),

    path('api/categories/', views.CategoryListCreateAPIView.as_view()),
    path('api/categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/products/', views.ProductListCreateAPIView.as_view()),
    path('api/products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view()),
]

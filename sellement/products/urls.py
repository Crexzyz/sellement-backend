from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from products import views


router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'categories', views.CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls))
]

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from products import views as product_views


router = DefaultRouter()
router.register(r'products', product_views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls))
]

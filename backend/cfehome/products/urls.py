from django.urls import path
from . import views
from .views import ProductDetailAPIView, ProductCreateAPIView, ProductDestroyAPIView, ProductUpdateAPIView



urlpatterns = [
    path('', views.ProductCreateAPIView.as_view()),
    path('<int:pk>/update/', views.ProductMixinView.as_view(), name="product-edit"),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="product-details"),
] 
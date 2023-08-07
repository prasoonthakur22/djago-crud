from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]

from VEGAN_API.VEGAN_API_PRODUCT.views import product_detail_view, ProductListView
from django.urls import path

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view_all_page'),
    #path('<str:category-slug>', product_list_view_by_category, name='product_list_view_all_page'),
    path('<str:slug>', product_detail_view, name='product_detail_view_page'),
]

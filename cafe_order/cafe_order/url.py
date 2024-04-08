# cafe/urls.py
from django.urls import path
from . import views

app_name='cafe_order'


urlpatterns = [
    path('', views.CategoryListView.as_view(), name="category_list"),
    path("<int:pk>/", views.CategoryDetailView.as_view(), name= "category_detail"),
    path("create/", views.ItemCreateView.as_view(), name='item_create'),
    path("delete/", views.ItemDeleteView.as_view(), name='item_delete'),
    ]
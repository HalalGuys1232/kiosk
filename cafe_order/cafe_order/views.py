
# cafe/views.py
from django.shortcuts import render
from .models import Category, Item, Order
from django.views.generic import *
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
class HomeView(TemplateView):
    template_name = "kiosk/main_cafe.html"

class ItemCreateView(CreateView):
    model = Item
    fields = ['category','Item_name', 'price']
    success_url = reverse_lazy('kiosk:category_list')
    template_name = 'kiosk/item_create.html'

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'kiosk/item_delete.html'
    def get_success_url(self):
        return reverse_lazy('kiosk:category_detail', kwargs={'pk': self.object.category.pk})
    
class CategoryListView(ListView):
    model = Category
    template_name = 'kiosk/category_list.html'

class CategoryDetailView(DetailView):
    model = Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_list'] = Item.objects.filter(category=self.object)
        return context
    template_name = 'kiosk/category_detail.html'
    
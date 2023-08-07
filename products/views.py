from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'description']
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')


from django.views.generic.list import ListView

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


from django.views.generic.edit import UpdateView

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'description']
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')
    

from django.views.generic.edit import DeleteView

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

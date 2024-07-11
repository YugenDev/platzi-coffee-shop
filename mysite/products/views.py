from django.views import generic
from .forms import ProductForm
from django.urls import reverse_lazy
from .models import Product
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    @csrf_exempt
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.FormView):
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products'







from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.
from .models import Product


class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context


def product_list_view(request):
	queryset = Products.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, "product/product_list_view.html", context)

class ProductDetailView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context


def product_detail_view(request, pk=None, *args, **kwargs):
	instance = Product.objects.get(pk=pk) #id
	queryset = Products.objects.all()
	context = {
		'object': instance
	}
	return render(request, "product/product_list_view.html", context)


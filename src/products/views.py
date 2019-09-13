from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import Product


class ProductListView(ListView):
	template_name = "products/list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()



def product_list_view(request):
	queryset = Products.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, "product/product_list_view.html", context)

class ProductDetailView(DetailView):
	#queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	# def get_object(self, *args, **kwargs):
	# 	request = self.request
	# 	pk = self.kwards.get('pk')
	# 	instance = Product.objects.get_by_id(pk)
	# 	if instance is None:
	# 		raise Http404("Product doesn't exist")
	# 	return instance

	def get_queryset(self, *args, **kwargs):
		request = self.request
		pk = self.kwards.get('pk')
		return Product.objects.filter(pk=pk)



def product_detail_view(request, pk=None, *args, **kwargs):
	instance = Product.objects.get(pk=pk) #id
	instance = get_object_or_404(Product, pk=pk)
	# try:
	# 	instaince = Product.objects.get(id=pk)
	# except Product.DoesNotExist:
	# 	print("No product")
	# 	raise Http404("Product doesn't exist")
	# except:
	# 	print("Huh?")

	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exist")
	# qs = Product.object.filter(id=pk)
	# if qs.exists() and qs.count() == 1:
	# 	instance = qs.first()
	# else:
	# 	raise Http404("Product doesn't exist")
	context = {
		'object': instance
	}
	return render(request, "product/product_list_view.html", context)


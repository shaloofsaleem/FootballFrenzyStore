from symbol import return_stmt
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect, render
from .models import *
from .form import *
from django.db.models import Q
# Create your views here.
class SearchResultsView(ListView):
    model = Product
    template_name = "user//base-layout.html"

  


def search(request):  # new
    if 'query' in request.GET:
        query = request.GET.get('query')
        if query:
            product=SubProductAttribute.objects.filter(product__product_name__icontains=query)
            category=Category.objects.all()
            brand=Brand.objects.all()
            color=Color.objects.all()
            context={
                'product':product,
                'category':category,
                'brand': brand,
                'color':color
            }
        
            return render(request, 'user/All Product/product.html', context)
        return HttpResponseRedirect('/')
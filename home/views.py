# from django.shortcuts import render
# from django.views import View
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from product.models import Product


# from product.models import Product


class HomeView(View):
    def get(self, request):
        product = Product.objects.all()
        recent_product = Product.objects.all().order_by('-created')[:4]
        print(recent_product)
        return render(request, 'home/index.html', context={'recent_product': recent_product, 'product': product})

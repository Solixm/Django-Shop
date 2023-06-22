from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from cart.cart_module import Cart
from product.models import Product


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_detail.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        storage, color, ram = request.POST.get('storage'), request.POST.get('color'), request.POST.get('ram')
        cart = Cart(request)
        cart.add(product, color, storage, ram)
        print(storage, color)
        return redirect('cart:detail')


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove(id)
        return redirect('cart:detail')

from product.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get[CART_SESSION_ID]
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            item['product'] = Product.objects.get(int(id=item['id']))
            yield item

    def unique_id_generator(self, id, color, storage, ram):
        result = f"{id}-{color}-{storage}-{ram}-"
        return result

    def add(self, product, color, storage, ram):
        unique = self.unique_id_generator(product.id, color, storage, ram)

        if unique not in self.cart:
            self.cart[unique] = {'price': str(product.price), 'color': color,
                                 'storage': str(storage), 'ram': str(ram), 'id': str(product.id)}

        self.save()

    def save(self):
        self.session.modified = True

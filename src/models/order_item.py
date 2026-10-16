class OrderItem:
    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("Ожидался экземпляр класса")
        self.product = product
        self.quantity = self._validate_quantity(quantity)

    @staticmethod
    def _validate_quantity(quantity):
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Указано неверное количество на покупку")
        return quantity

    def get_total_price(self):
        return self.product.price * self.quantity
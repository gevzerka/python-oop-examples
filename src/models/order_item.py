from decimal import Decimal
from src.models.product import Product
from src.validators import validate_quantity

class OrderItem:
    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(product, Product):
            raise TypeError("product должен быть экземпляром класса Product")
        self._product = product
        self._quantity = validate_quantity(quantity)
        self._unit_price = product.price

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def unit_price(self) -> Decimal:
        return self._unit_price

    def get_total_price(self) -> Decimal:
        return self._unit_price * self._quantity

    def __repr__(self) -> str:
        return f'OrderItem(product={self._product.name!r}, quantity={self._quantity})'
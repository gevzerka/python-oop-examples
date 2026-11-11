from collections import defaultdict
from decimal import Decimal
from src.exceptions import EmptyOrderError, OrderAlreadyPlacedError, OutOfStockError
from src.models.customer import Customer
from src.models.product import Product
from src.models.order_item import OrderItem

class Order:
    def __init__(self, customer: Customer) -> None:
        if not isinstance(customer, Customer):
            raise TypeError("customer должен быть экземпляром Customer")
        self._customer = customer
        self._items: list[OrderItem] = []
        self._is_placed = False

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def is_placed(self) -> bool:
        return self._is_placed

    @property
    def items(self) -> tuple[OrderItem, ...]:
        return tuple(self._items)

    def add_item(self, product: Product, quantity: int) -> None:
        if self._is_placed:
            raise OrderAlreadyPlacedError("Нельзя изменить оформленный заказ")
        self._items.append(OrderItem(product, quantity))

    def get_total_price(self) -> Decimal:
        return sum((item.get_total_price() for item in self.items), Decimal('0'))

    def get_items_count(self) -> int:
        return sum(item.quantity for item in self.items)

    def place_order(self) -> None:
        if self._is_placed:
            raise OrderAlreadyPlacedError("Заказ уже оформлен")
        if not self._items:
            raise EmptyOrderError("Нельзя оформить пустой заказ")

        positions: dict[Product, int] = defaultdict(int)
        for item in self._items:
            positions[item.product] += item.quantity

        purchased: list[tuple[Product, int]] = []
        try:
            for product, quantity in positions.items():
                product.purchase(quantity)
                purchased.append((product, quantity))
        except OutOfStockError:
            for product, quantity in purchased:
                product.restock(quantity)
            raise

        self._is_placed = True

    def __repr__(self) -> str:
        status = 'Оформлен' if self._is_placed else 'Новый'
        return f'Order(customer={self._customer.name!r}, items={len(self._items)},  {status}'
from decimal import Decimal
from src.validators import validate_quantity
from src.exceptions import OutOfStockError
class Product:
    def __init__(self, name: str, price: int | float | Decimal, stock: int) -> None:
        self.name = name
        self.price = price
        self._stock = self._validate_stock(stock)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = self._validate_name(value)

    @property
    def price(self) -> Decimal:
        return self._price

    @price.setter
    def price(self, value: int | float | Decimal) -> None:
        self._price = self._validate_price(value)

    @property
    def stock(self) -> int:
        return self._stock

    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название должно быть непустой строкой")
        return name.strip()

    @staticmethod
    def _validate_price(price: int | float | Decimal) -> Decimal:
        if type(price) is bool or not isinstance(price, (int, float, Decimal)):
            raise ValueError("Цена должна быть числом")
        value = Decimal(str(price))
        if not value.is_finite() or value <= 0:
            raise ValueError("Цена должна быть больше нуля")
        return value

    @staticmethod
    def _validate_stock(stock: int) -> int:
        if type(stock) is not int or stock < 0:
            raise ValueError("Остаток должен быть больше нуля")
        return stock

    def is_available(self, quantity: int) -> bool:
        return self._stock >= validate_quantity(quantity)

    def purchase(self, quantity: int) -> None:
        quantity = validate_quantity(quantity)
        if quantity > self._stock:
            raise OutOfStockError(self._name, quantity, self._stock)
        self._stock -= quantity

    def restock(self, quantity: int) -> None:
        self._stock += validate_quantity(quantity)

    def __repr__(self) -> str:
        return f'Product(name={self._name!r}, price={self._price}, stock={self._stock})'
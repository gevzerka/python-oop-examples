class ShopError(Exception):
    """Базовое исключение"""

class OutOfStockError(ShopError):
    def __init__(self, product_name: str, requested: int, available: int) -> None:
        self.product_name = product_name
        self.requested = requested
        self.available = available
        super().__init__(
            f'Недостаточно товара "{product_name}": '
            f'запрошено {requested}, в наличии {available}'
        )

class EmptyOrderError(ShopError):
    """Нельзя оформить пустой заказ"""

class OrderAlreadyPlacedError(ShopError):
    """Закакз уде оформлен и больше не может изменяться"""
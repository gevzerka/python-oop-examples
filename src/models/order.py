from src.models.customer import Customer
from src.models.product import Product
from src.models.order_item import OrderItem

class Order:
    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customer должен быть экземпляром Customer")
        self.customer = customer

        self.is_placed = False
        self.items = []

    def add_item(self, product, quantity):
        if not self.is_placed:
            self.items.append(OrderItem(product, quantity))
        else: raise ValueError("Нельзя изменить оформленный заказ")

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items)

    def get_items_count(self):
        return sum(item.quantity for item in self.items)

    def place_order(self):
        if not self.items or self.is_placed: return False

        positions = {}
        for item in self.items:
            if item.product in positions:
                positions[item.product] += item.quantity
            else:
                positions[item.product] = item.quantity

        for product, quantity in positions.items():
            if not product.is_available(quantity):
                return False

        #TODO Переписать логику, чтоб после False делался откат в предыдущих позициях
        for product, quantity in positions.items():
            if not product.purchase(quantity):
                return False

        self.is_placed = True
        return True
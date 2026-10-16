class Order:
    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customer должен быть экземпляром Customer")
        self.customer = customer

        self.items = []

    def add_item(self, product, quantity):
        self.items.append(OrderItem(product, quantity))

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items)

    def get_items_count(self):
        return sum(item.quantity for item in self.items)

    def place_order(self):
        if not self.items: return False

        positions = {}
        for item in self.items:
            if item.product in positions:
                positions[item.product] += item.quantity
            else:
                positions[item.product] = item.quantity

        for key, val in positions.items():
            if not key.is_available(val):
                return False

        for key, val in positions.items():
            key.purchase(val)
        return True
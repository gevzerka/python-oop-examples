import pytest

from src.models.product import Product
from src.models.customer import Customer
from src.models.order import Order

class TestOrder:
    def test_create_order_object(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')

        with pytest.raises(TypeError):
            order = Order('a')

        order = Order(customer)

        assert not order.items
        assert order.customer == customer

    def test_add_item(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 10)
        order = Order(customer)

        with pytest.raises(TypeError):
            order.add_item(customer, 5)

        with pytest.raises(ValueError):
            order.add_item(water, -5)

        order.add_item(water, 5)

        assert order.items[0].product == water
        assert order.items[0].quantity == 5

    def test_get_total_price(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 10)
        pizza = Product('Pepperoni', 120, 4)
        order = Order(customer)
        order.add_item(water, 2)
        order.add_item(pizza, 2)
        res = order.get_total_price()
        assert res == 350

    def test_items_count(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 10)
        pizza = Product('Pepperoni', 120, 4)
        order = Order(customer)
        order.add_item(water, 2)
        order.add_item(pizza, 4)
        res = order.get_items_count()
        assert res == 6

    def test_positive_place_order(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 10)
        pizza = Product('Pepperoni', 120, 4)
        order = Order(customer)
        order.add_item(water, 2)
        order.add_item(pizza, 4)
        res = order.place_order()
        assert res is True
        assert water.stock == 8
        assert pizza.stock == 0

    def test_negative_place_order(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 10)
        pizza = Product('Pepperoni', 120, 4)
        order = Order(customer)
        order.add_item(water, 2)
        order.add_item(pizza, 6)
        res = order.place_order()
        assert res is False
        assert water.stock == 10
        assert pizza.stock == 4

    def test_positive_place_order_two_positions(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 10)
        order = Order(customer)
        order.add_item(water, 2)
        order.add_item(water, 5)
        res = order.place_order()
        assert res is True
        assert water.stock == 3

    def test_negative_place_order_two_positions(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 10)
        order = Order(customer)
        order.add_item(water, 7)
        order.add_item(water, 5)
        res = order.place_order()
        assert res is False
        assert water.stock == 10

    def test_place_order_again(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 10)
        order = Order(customer)
        order.add_item(water, 2)
        order.add_item(water, 5)
        res = order.place_order()
        res_again = order.place_order()
        assert res is True
        assert res_again is False
        assert water.stock == 3

    def test_negative_again_add_item_after_order(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 10)
        order = Order(customer)
        order.add_item(water, 2)
        res = order.place_order()
        with pytest.raises(ValueError):
            order.add_item(water, 5)
        assert res is True
        assert order.is_placed is True
        assert water.stock == 8

    def test_place_order_false(self):
        customer = Customer('Dima', 'dimaexample@gmail.com')
        water = Product('Coca-Cola', 55, 5)
        order = Order(customer)
        order.add_item(water, 7)
        res = order.place_order()
        assert res is False
        assert order.is_placed is False
        assert water.stock == 5
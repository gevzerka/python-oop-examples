import pytest
from src.models.product import Product

class TestProduct:
    def test_negative_validate_name1(self):
        with pytest.raises(ValueError):
            negative_name = Product(1, 55, 3)  # Должен выкидвать ValueError из-за того, что name не str

    def test_negative_validate_name2(self):
        with pytest.raises(ValueError):
            name_only_space = Product('     ', 55, 3)

    def test_negative_validate_price1(self):
        with pytest.raises(ValueError):
            bool_price = Product('Coca-Cola', True,
                                 10)  # Должен выкидвать ValueError из-за того, что price не int or float

    def test_negative_validate_price2(self):
        with pytest.raises(ValueError):
            negative_price = Product('LADA', -10, 1)

    def test_negative_validate_stock1(self):
        with pytest.raises(ValueError):
            negative_stock = Product('Coca-Cola', 55, -2)

    def test_negative_validate_stock2(self):
        with pytest.raises(ValueError):
            not_int_stock = Product('LADA', 10, True)

    def test_positive_validate(self):
        product = Product('Coca-Cola', 55, 3)
        assert product.name == 'Coca-Cola'
        assert product.price == 55
        assert product.stock == 3

    def test_positive_change_price(self):
        product = Product('Coca-Cola', 55, 3)
        product.change_price(70)
        assert product.price == 70

    def test_negative_change_price(self):
        product = Product('Coca-Cola', 55, 3)
        with pytest.raises(ValueError):
            product.change_price(-90)
        assert product.price == 55

    def test_positive_is_avaliable(self):
        product = Product('Coca-Cola', 55, 3)
        res = product.is_available(2)
        assert res is True

    def test_negative_is_avaliable(self):
        product = Product('Coca-Cola', 55, 3)
        res = product.is_available(10)
        assert res is False

    def test_purchase(self):
        product = Product('Coca-Cola', 55, 10)
        product.purchase(5)
        assert product.stock == 5

    def test_negative_purchase1(self):
        product = Product('Coca-Cola', 55, 10)
        res = product.purchase(12)
        assert res is False
        assert product.stock == 10

    def test_negative_purchase2(self):
        product = Product('Coca-Cola', 55, 10)
        with pytest.raises(ValueError):
            res = product.purchase(0)
        assert product.stock == 10
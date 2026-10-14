class Product:
    def __init__(self, name, price, stock):
        self.name = self._validate_name(name)
        self.price = self._validate_price(price)
        self.stock = self._validate_stock(stock)

    def _validate_name(self, name):
        if not isinstance(name, str) or len(name.strip()) < 1:
            raise ValueError("Название должно быть строкой длиной не менее одного символа")
        else:
            return name.strip()

    def _validate_price(self, price):
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Задано неверное значение цены")
        else:
            return price

    def _validate_stock(self, stock):
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("Задано неверное количество товара")
        else:
            return stock

    def change_price(self, new_price):
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            raise ValueError("Указано неверное значение новой цены")
        else:
            self.price = new_price

    def is_available(self, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Указано неверное значение кол-ва")
        elif self.stock < quantity:
            return False
        else:
            return True

    def purchase(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        else:
            return False
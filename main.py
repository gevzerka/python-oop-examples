from src.models.product import Product
from src.models.customer import Customer
from src.models.order import Order

def main():
    coca_cola = Product('Coca-Cola', 55, 30)
    pepperoni = Product('Pepperoni', 120, 30)
    soup = Product('Soup', 90, 30)

    dima = Customer('Dima', 'dimaexample@gmail.com')
    vova = Customer('Vovchik', 'kakoy_vovchik@gmail.com')

    order_dima = Order(dima)
    order_vova = Order(vova)

    order_dima.add_item(coca_cola, 4)
    order_dima.add_item(coca_cola, 2)
    order_dima.add_item(soup, 7)

    order_vova.add_item(coca_cola, 6)
    order_vova.add_item(pepperoni, 5)

    order_dima.add_item(coca_cola, 10)
    res_dima = order_dima.place_order()

    res_vova = order_vova.place_order()

    print(res_dima, res_vova)

if __name__ == "__main__":
    main()
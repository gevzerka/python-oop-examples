from src.exceptions import OutOfStockError
from src.models.product import Product
from src.models.customer import Customer
from src.models.order import Order

def print_stock(*products: Product) -> None:
    print("Остатки:", ", ".join(f'{p.name} - {p.stock}' for p in products))

def main():
    coca_cola = Product('Coca-Cola', 55, 30)
    pepperoni = Product('Pepperoni', 120, 30)
    soup = Product('Soup', 90, 30)

    dima = Customer('Dima', 'dimaexample@gmail.com')
    vova = Customer('Vovchik', 'kakoy_vovchik@gmail.com')

    order_dima = Order(dima)
    order_dima.add_item(coca_cola, 4)
    order_dima.add_item(coca_cola, 2)
    order_dima.add_item(soup, 7)

    order_vova = Order(vova)
    order_vova.add_item(coca_cola, 6)
    order_vova.add_item(pepperoni, 5)

    print_stock(coca_cola, pepperoni, soup)

    for order in (order_dima, order_vova):
        order.place_order()
        print(
            f"{order.customer.name}: {order.get_items_count()} шт., "
            f"итого {order.get_total_price()}"
        )

    print_stock(coca_cola, pepperoni, soup)

    greedy = Order(vova)
    greedy.add_item(pepperoni, 3)
    greedy.add_item(coca_cola, 100)
    try:
        greedy.place_order()
    except OutOfStockError as error:
        print(f'Заказ не оформлен: {error}')
    print_stock(coca_cola, pepperoni, soup)

if __name__ == "__main__":
    main()
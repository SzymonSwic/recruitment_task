from dataclasses import dataclass
import heapq

@dataclass
class Order:
    order_id: str
    order_type: str
    price: float
    quantity: int

    def __post_init__(self):
        self.heap_compare_value: float = self.price if self.order_type == 'Sell' else -self.price

    def __lt__(self, other):
        return self.heap_compare_value < other.heap_compare_value


class OrderRegister:
    def __init__(self):
        self.buy_orders = []  # Max heap for buy orders
        self.sell_orders = []  # Min heap for sell orders

    def add_order(self, order):
        if order.order_type == 'Buy':
            heapq.heappush(self.buy_orders, order)
        elif order.order_type == 'Sell':
            heapq.heappush(self.sell_orders, order)

    def remove_order(self, order_id, order_type, price, quantity):
        order = Order(order_id, order_type, price, quantity)

        if order_type == 'Buy' and order in self.buy_orders:
            self.buy_orders.remove(order)
            heapq.heapify(self.buy_orders)
        elif order_type == 'Sell' and order in self.sell_orders:
            self.sell_orders.remove(order)
            heapq.heapify(self.sell_orders)

    def display_best_prices(self):
        best_buy_price = self.buy_orders[0].price if self.buy_orders else None
        best_sell_price = self.sell_orders[0].price if self.sell_orders else None

        print("Best Buy Price:", best_buy_price, "Orders:",
              [order for order in self.buy_orders])
        print("Best Sell Price:", best_sell_price, "Orders:",
              [order for order in self.sell_orders])


if __name__ == '__main__':
    orders = OrderRegister()

    orders.add_order(Order("001", "Buy", 20.00, 100))
    orders.add_order(Order("002", "Sell", 25.00, 200))
    orders.add_order(Order("003", "Buy", 23.00, 50))
    orders.add_order(Order("004", "Buy", 23.00, 70))
    orders.remove_order("003", "Buy", 23.00, 50)
    orders.add_order(Order("005", "Sell", 28.00, 100))

    orders.display_best_prices()

# order.py
class Order:
    def __init__(self, customer, restaurant):
        self.customer = customer
        self.restaurant = restaurant
        self.items = {}
        self.status = "Em preparo"
        self.payment_method = None

    def add_item(self, item, quantity):
        if item in self.restaurant.menu._dishes:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity
        else:
            raise ValueError(f"Item '{item}' não encontrado no menu.")

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            raise ValueError(f"Item '{item}' não encontrado no pedido.")

    def calculate_total(self):
        total = 0
        for item, quantity in self.items.items():
            total += self.restaurant.menu._dishes[item] * quantity
        return total

    def display_order(self):
        order_details = "\n".join([f"{item}: {quantity}x" for item, quantity in self.items.items()])
        return f"Pedido de {self.customer.name}:\n{order_details}\nTotal: R${self.calculate_total():.2f}"

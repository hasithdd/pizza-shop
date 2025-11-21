from order import Order

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.order: Order | None = None

    def place_order(self, pizza_type: str) -> Order:
        self.order = Order(pizza_type=pizza_type)
        return self.order
    
    def __repr__(self):
        return f"Customer(name={self.name}, order={self.order})"
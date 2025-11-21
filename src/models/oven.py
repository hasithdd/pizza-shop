from order import Order
from collections import deque

class Oven:
    def __init__(self):
        self.current_pizza: Order | None = None
        self.waiting_queue = deque()

    def enqueue(self, order: Order):
        if self.current_pizza is None:
            self.current_pizza = order
            order.mark_baking()
        else:
            self.waiting_queue.append(order)

    def bake_next(self):
        if self.current_pizza is not None:
            self.current_pizza.mark_done()
        
        if self.waiting_queue:
            next_order = self.waiting_queue.popleft()
            self.current_pizza = next_order
            next_order.mark_baking()
        else:
            self.current_pizza = None

    def __repr__(self):
        return (f"Oven(current_pizza={self.current_pizza}, "
                f"waiting_queue={list(self.waiting_queue)})")
    
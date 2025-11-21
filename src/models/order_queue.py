from collections import deque
from order import Order

class OrderQueue:
    def __init__(self):
        self.walk_in = deque()
        self.online = deque()

    def add_order(self, order: Order, is_online: bool):
        if is_online:
            self.online.append(order)
        else:
            self.walk_in.append(order)
    
    def get_next(self) -> Order | None:
        if self.walk_in:
            return self.walk_in.popleft()
        elif self.online:
            return self.online.popleft()
        else:
            return None
        
    def __repr__(self):
        return(f"OrderQueue("
               f"walk_in={list(self.walk_in)}, "
               f"online={list(self.online)})")
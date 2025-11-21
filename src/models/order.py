class Order:
    def __init__(self, pizza_type: str):
        self.pizza_type = pizza_type
        self.payment_status = "Pending"
        self.baking_status = "Waiting"
    
    def mark_paid(self):
        self.payment_status = "Paid"
    
    def mark_baking(self):
        self.baking_status = "Baking"

    def mark_done(self):
        self.baking_status = "Done"
        
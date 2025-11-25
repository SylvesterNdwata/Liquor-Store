

class Invoice:
    def __init__(self):
        self.items = []
        self.total_cost = 0.0
        
    def add_item(self, item_price):
        self.total_cost += item_price


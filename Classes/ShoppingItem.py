class ShoppingItem:
    def __init__(self, name, price, quantity):
            self.name = name
            self.price=price
            self.quantity = quantity
            
    def total_cost(self):
            return self.price * self.quantity       
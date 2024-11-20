from ShoppingItem import *

cart = ShoppingItem('Laptop', 1200, 2)
print(f'the cost of {cart.quantity} {cart.name} is  {cart.total_cost()}')
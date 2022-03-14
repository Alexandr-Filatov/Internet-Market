from User import *
from Item import *
from Order import *

alex = User('Alex', 'Filatov', '+79234524562')
print(alex)
pencil = Item('Pencil', 15)
pen = Item('Pen', 12)
table = Item('Table', 34)
print(table)
ord1 = Order(1, [pencil, pen, table])
ord1.total_price_calculate()
print(ord1)
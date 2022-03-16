from User import *
from Item import *
from Order import *
from Catalog import *

# Создание пользователя
alex = User('Alex', 'Filatov', '+79234524562')
print(alex)

# Создание товаров
pencil = Item('Pencil', 15)
pen = Item('Pen', 12)
table = Item('Table', 34)
print(table)

# Создание заказа
ord1 = Order(1, [pencil, pen, table])
ord1.total_price_calculate()
print(ord1)

# Создание каталога
catalog1 = Catalog('Office supplies', [pencil, pen])
catalog2 = Catalog('Furniture', [table])
print(catalog1)
print(catalog2)

# Добавление товаров в существующие каталог
chair = Item('Chair', 23)
catalog2.add_item(chair)
print(catalog2)

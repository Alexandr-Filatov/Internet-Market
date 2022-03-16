import datetime
from User import user_line_begin, user_line_end

class Item(object):

    __last_id = 0
    __list = list()

    def __init__(self, title, price):
        Item.__last_id += 1
        self.id = Item.__last_id
        self.title = title
        self.price = price
        self.created = datetime.datetime.now()
        Item.__list.append(self)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return user_line_begin + "\n" + "Item ID: " + str(self.id) + "\n" + "Item title: " + self.title + "\n" + "Item price: " + str(self.price) + "\n" + user_line_end
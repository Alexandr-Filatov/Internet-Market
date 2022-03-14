import datetime


class Order(object):

    __last_id = 0
    __list = list()

    def __init__(self, user_id, order_list):
        Order.__last_id += 1
        self.id = Order.__last_id
        self.created = datetime.datetime.now()
        self.total_price = 0
        self.user_id = user_id
        self.order_list = order_list
        Order.__list.append(self)

    def total_price_calculate(self):
        for item in self.order_list:
            self.total_price += item.price


    def __str__(self):
        return "\n************\n" + "Order ID: " + str(self.id) + "\n" + "Total price: " + str(self.total_price) + "\n"+ "User ID: " + str(self.user_id) + "\n" + "Date created: " + str(self.created) + "\n************\n"
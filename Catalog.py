from User import user_line_begin, user_line_end
class Catalog(object):

    __last_id = 0
    __list = list()

    def __init__(self, catalog_name, item_list):
        Catalog.__last_id += 1
        self.id = Catalog.__last_id
        self.catalog_name = catalog_name
        self.__item_list = item_list
        Catalog.__list.append(self)

    def add_item(self, item):
        return self.__item_list.append(item)

    def __str__(self):
        print(user_line_begin + "\n" + self.catalog_name + ":")
        print("Catalog ID: " + str(self.id), end = '' )
        print(user_line_begin)
        print("Content:")
        for item in self.__item_list:
            print(str(item.title) + ", " + "ID: " + str(item.id) + ", " + "Price: " + str(item.price))
        return user_line_end

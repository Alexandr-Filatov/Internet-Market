import datetime

user_line_begin = "\n********************************************************"
user_line_end = "********************************************************\n"

class User(object):
    
    __last_id = 0
    __list = list()


    def __init__(self, name, surname, phone):
        User.__last_id += 1
        self.id = User.__last_id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.created = datetime.datetime.now()
        User.__list.append(self)

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @staticmethod
    def get_user_by_id(self, id):
        for user in User.__list:
            if user.id == id:
                return user
        raise ValueError('User not found')

    @staticmethod
    def get_user_by_phone(self, phone):
        for user in User.__list:
            if user.phone == phone:
                return user
        raise ValueError('User not found')

    def __str__(self):
        return user_line_begin + "\n" + "User ID: " + str(self.id) + "\n" + "User name: " + self.name + "\n" + "User surname: " + self.surname + "\n" + "User phone: " + str(self.phone) + "\n" + user_line_end
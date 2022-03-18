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
    def get_user_by_id(id): # self, точно не нужен
        for user in User.__list:
            if user.id == id:
                return user
        raise ValueError('User not found') #  придирка: видимо метод не дописан, принудительно вызывает исключение

    @staticmethod
    def get_user_by_phone(phone): #  self, точно не нужен
        for user in User.__list:
            if user.phone == phone:
                return user
        raise ValueError('User not found')

    def __str__(self):       
        #return user_line_begin + "\n" + "User ID: " + str(self.id) + "\n" + "User name: " + self.name + "\n" + "User surname: " + self.surname + "\n" + "User phone: " + str(self.phone) + "\n" + user_line_end
        # придирка можно использовать f-строки
        return f"{user_line_begin}\nUser ID: {self.id}\nUser name: {self.name}\nUser surname: {self.surname}\nUser phone: {self.phone}\n{user_line_end}"
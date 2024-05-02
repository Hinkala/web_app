from flask_login import UserMixin


class Cat:
    def __init__(self, cat_id, name, fur, age, img):
        self.cat_id = cat_id
        self.name = name
        self.fur = fur
        self.age = age
        self.img = img


class Credentials:
    def __init__(self, id, login, password, user_id):
        self.id = id
        self.login = login
        self.password = password
        self.user_id = user_id


class User(UserMixin):
    def __init__(self, id, name, surname, patronymic):
        self.id = id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic


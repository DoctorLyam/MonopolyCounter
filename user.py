from base_class import Base
from area import Area, First_1, First_2, Areas

class User(Area):
    def __init__(self, name, areas, budget):
        self.name = name
        self.areas = areas
        self.budget = budget
        self.areas_obj = Areas()

    # Покупка участка
    def buy_area(self, area):
        if (area.name in self.areas_obj.areas_list) and (area not in self.areas) and (self.budget >= area.price):
            print(f'Общий спиок предприятий ДО приобретения: {self.areas_obj.areas_list}')
            self.areas_obj.areas_list.remove(area.name)
            print(f'Общий спиcок предприятий ПОСЛЕ приобретения: {self.areas_obj.areas_list}')
            self.areas[area.name] = 0
            self.budget -= brown_one.price
            print(f"Игроку {self.name} добавлен участок {area.name}. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.areas}")
        elif area not in self.areas and self.budget < brown_one.price:
            print(f"Стоимость участка '{area.name}' слишком велика")
        elif area in self.areas:
            print(f'Участок уже принадлежит игроку {self.name}')
        elif area.name not in self.areas_obj.areas_list:
            print(f"Участка {area.name} уже нет в общем списке участков")

    # Заложение участка
    def dep_area(self, area):
        if (area.name in self.areas) and (self.areas[area.name]) == 0:
            self.areas[area.name] = -1
            self.budget += area.deposite
            print(f'Участок {area.name} заложен. Баланс {self.name} равен {self.budget}. \nВ собственности {self.name} находятся: {self.areas}')
        elif area.name not in self.areas:
            print(f'Участок недоступен для заложения {self.name}, потому что его нет в списке приобретенных участков')
        elif self.areas[area.name] == -1:
            print(f'{self.name} уже заложил этот участок ранее')
        elif self.areas[area.name] >= 1:
            print(f'Участок {area.name} имеет филиал(-ы) или предприятие. Сначала следует продать их')
        


user_1 = User(name="Саша", areas={}, budget=2000)
user_2 = User(name="Настя", areas={}, budget=2000)

brown_one = First_1(name='Дом Гарри', price=60, deposite=30, rent_stock=2, 
            rent_one_off=10, rent_two_off=30, rent_three_off=90, rent_four_off=160, rent_firm=250)
brown_two = First_1(name='Вокзал Кингс-Кросс', price=60, deposite=30, rent_stock=4, 
            rent_one_off=20, rent_two_off=60, rent_three_off=180, rent_four_off=320, rent_firm=450)

user_1.buy_area(brown_one)
user_1.dep_area(brown_one)
user_1.dep_area(brown_one)
from base_class import Base
from area import Area, First_1, First_1_son, First_2, First_2_son, Areas

class User(Area):
    def __init__(self, name, areas, budget, bolshoy_dyadya=[]):
        self.name = name
        self.areas = areas
        self.budget = budget
        self.bolshoy_dyadya = bolshoy_dyadya
        self.areas_obj = Areas()
        self.First_1 = First_1_son()
        self.First_2 = First_2_son()

    # Покупка участка
    def buy_area(self, area):
        # Если покупаемый участок есть в общем списке участков
        # и если этого участка еще нет в списке покупающего его юзера
        # и если бюджет позволяет
        if (area.name in self.areas_obj.areas_list) and (area not in self.areas) and (self.budget >= area.price):
            print(f'Общий список предприятий ДО приобретения: {self.areas_obj.areas_list}')
            self.areas_obj.areas_list.remove(area.name)
            print(f'Общий спиcок предприятий ПОСЛЕ приобретения: {self.areas_obj.areas_list}')
            self.areas[area.name] = 0
            self.budget -= brown_one.price
            print(f"Игроку {self.name} добавлен участок {area.name}. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.areas}")
            # Через имя класса участка получаем значение атрибута объекта user - First = First_son
            class_name = type(area).__name__
            class_attr = getattr(self, class_name, None)
            # Добавляю участки, принадлежащие данной отрасли, в пустой список
            # чтобы сравнить длину списка с заданным значением в классе
            # Это поможет понять, является ли юзер обладаетелем всей отрасли
            temp_list = []
            for uchastok in self.areas:
                if uchastok in class_attr.areas_list:
                    temp_list.append(uchastok)
            if len(temp_list) == class_attr.areas_count:
                print(f'Отрасль целиком принадлежит {self.name}')
                self.bolshoy_dyadya.append(class_attr.name)
                print(f'Игроку {self.name} принадлежат отрасли: {self.bolshoy_dyadya}')
            else:
                pass
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
user_1.buy_area(brown_two)
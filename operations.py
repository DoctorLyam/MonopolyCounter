from area import Area, Transport, Support, First_1, First_1_son, First_2, First_2_son, Second_1, Second_1_son, Second_2, Second_2_son, Third_1, Third_1_son, Third_2, Third_2_son, Fourth_1, Fourth_1_son, Fourth_2, Fourth_2_son
from random import randint

# Статусы участков:
# -1 - заложен; 0 - куплен; 1,2,3,4 - установлен(-ы) филиал(-ы); 5 - установлено предприятие 

class User(Area):
    areas_list = ['Дом Гарри', 'Вокзал Кингс-Кросс', 'Отдел магического транспорта', 'Отдел тайн', 'Отдел обеспечения магического правопорядка',
                  'Магазин Совы', 'Лавка Олливандера', 'Всё для Квиддича', 'Три метлы', 'Кабанья голова', 'Сладкое королевство',
                  'Большой зал', 'Выручай Комната', 'Хижина Хагрида', 'Карта Мародёров', 'Маховик времени', 'Меч Гриффиндора',
                  'Бузинная палочка', 'Воскрешающий камень', 'Мантия-Невидимка', 'Придира', 'Ежедневный пророк']
    transport_list = ['Хогвартс-Экспресс', 'Летающая метла', 'Летучий порох', 'Магический портал']
    support_list = ['Добби', 'Кикимер']

    def __init__(self, name, areas, transps, sups, budget: int, bolshoy_dyadya=[]):
        self.name = name
        self.areas = areas
        self.transps = transps
        self.sups = sups
        self.budget = budget
        self.bolshoy_dyadya = bolshoy_dyadya
        self.First_1 = First_1_son()
        self.First_2 = First_2_son()
        self.Second_1 = Second_1_son()
        self.Second_2 = Second_2_son()
        self.Third_1 = Third_1_son()
        self.Third_2 = Third_2_son()
        self.Fourth_1 = Fourth_1_son()
        self.Fourth_2 = Fourth_2_son()

    # Удаление участка из общего списка участков
    @classmethod
    def del_area_from_gen_list(cls, typel):
        if type(typel).__name__ == ('First_1' or 'First_2' or 'Second_1' or 'Second_2' or 'Third_1' or 'Third_2' or 'Fourth_1' or 'Fourth_2'):
            return cls.areas_list.remove(typel.name)
        elif type(typel).__name__ == 'Transport':
            return cls.transport_list.remove(typel.name)
        elif type(typel).__name__ == 'Support':
            return cls.support_list.remove(typel.name)


    # Взять деньги из банка
    def get_money_from_bank(self, money: int):
        self.budget += money
        print(f'{self.name} получил {money} галлеонов из банка.\nБюджет {self.name} составляет {self.budget}')

    # Дать деньги
    def give_money_to_bank(self, money: int):
        if self.budget >= money:
            self.budget -= money
            print(f'{self.name} отдал {money} галлеонов банку.\nБюджет {self.name} составляет {self.budget}')
        elif 0 < self.budget < money:
            print(f'В бюджете {self.name} нет таких денег. Введите сумму поменьше')
        elif self.budget == 0:
            print(f'В бюджете {self.name} совсем нет денег')


    # Круговой доход
    def cicle_add(self):
        self.budget += 200
        print(f'Получен круговой доход. Бюджет {self.name} равен {self.budget}')

    # Налог
    def nalog(self):
        if self.budget >= 200:
            self.budget -= 200
            print(f'{self.name} платит налог. Бюджет {self.name} равен {self.budget}')
        else: print(f'{self.name} недостаточно денег оплаты налога')
    
    # Попадание в тюрьму
    def prison(self):
        if self.budget >= 50:
            self.budget -= 50
            print(f'{self.name} платит за выход из тюрьмы. Бюджет {self.name} равен {self.budget}')
        else: print(f'{self.name} недостаточно денег для выхода на свободу')

    # Покупка участка
    def buy_area(self, area):
        # Если покупаемый участок есть в общем списке участков
        # и если этого участка еще нет в списке покупающего его юзера
        # и если бюджет позволяет
        if (area.name in User.areas_list) and (area.name not in self.areas) and (self.budget >= area.price):
            print(f'Общий список предприятий ДО приобретения: {User.areas_list}')
            User.del_area_from_gen_list(area)
            print(f'Общий спиcок предприятий ПОСЛЕ приобретения: {User.areas_list}')
            self.areas[area.name] = 0
            self.budget -= area.price
            # Присваиваю участку в качестве атрибута объект Юзер, чтобы
            # через участок можно было обращаться к самому Юзеру и его атрибутам
            area.owner = self
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
        elif (area.name in User.areas_list) and (area.name not in self.areas) and (self.budget < area.price):
            print(f"Стоимость участка '{area.name}' слишком велика")
        elif (area.name in self.areas) and (self.areas[area.name] >= 0):
            print(f'Участок {area.name} уже принадлежит игроку {self.name}')
        elif (area.name not in self.areas) and (area.name not in User.areas_list):
            print(f"Участка {area.name} уже нет в общем списке участков. Он находится в собственности {area.owner.name}")

    # Заложение участка
    def dep_area(self, area):
        class_name = type(area).__name__
        class_attr = getattr(self, class_name, None)

        if area.name in self.areas:
            temp_list2 = []
            for k in self.areas:
                if (k in class_attr.areas_list):
                    temp_list2.append(self.areas[k])
            if temp_list2:
                if ((1 or 2 or 3 or 4 or 5) not in temp_list2) and (self.areas[area.name] == 0):
                    self.areas[area.name] = -1
                    self.budget += area.deposite
                    print(f'Участок {area.name} заложен. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.areas}')
                elif self.areas[area.name] == -1:
                    print(f'{self.name} уже заложил этот участок ранее')
                elif self.areas[area.name] >= 1:
                    print(f'Участок {area.name} имеет филиал(-ы) или предприятие. Сначала следует продать их')
                else:
                    print(f'На другом участке отрасли {class_attr.name} есть филиалы и/или предприятия. Игроку {self.name} не удалось заложить участок {area.name}')
            else:
                print(f'Заложение участка {area.name} игроком {self.name} невозможно')
        else: print(f'{area.name} нет в списке участков игрока {self.name}. Участок недоступен для заложения')

    # Выкуп заложенного участка
    def get_dep_area(self, area):
        # Если заложенный участок есть в списке юзера
        # и если значение ключа для этого участка -1
        # и если позволяет бюджет
        if (area.name in self.areas) and (self.areas[area.name] == -1) and (self.budget >= (area.deposite+0.1*area.deposite)):
            self.areas[area.name] = 0
            self.budget -= area.deposite+0.1*area.deposite
            print(f'{self.name} выкупил заложенный участок. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.areas}')
        elif area.name not in self.areas:
            print(f'Участок {area.name} не принадлежит {self.name}')
        elif self.areas[area.name] >= 0:
            print(f'{self.name} уже имеет {area.name} в собственности, участок не под залогом')
        elif (area.name in self.areas) and (self.areas[area.name] == -1) and (self.budget < (area.deposite+0.1*area.deposite)):
            print(f'{self.name} не может выкупить {area.name} из залога, потому что в его бюджете недостаточно средств')

    # Покупка офиса
    def get_office(self, area):
        class_name = type(area).__name__
        class_attr = getattr(self, class_name, None)
        temp_list = []
        for uchastok in self.areas:
            if uchastok in class_attr.areas_list:
                temp_list.append(uchastok)

        # Вычленяю из словаря с участками участки данной отрасли без данного участка
        # чтобы найти минимальное значение и отнять его от значения данного участка
        # По этой разнице узнаю, можно ли устанавливать филиал на данном участке
        # т.к. если разница = 1, значит прежде филиалы надо устанавить на других участках этой отрасли 
        if area.name in self.areas:
            temp_list2 = []
            for k in self.areas:
                if (k in class_attr.areas_list) and (k != area.name):
                    temp_list2.append(self.areas[k])
            if temp_list2:
                min_off = min(temp_list2)
                difference = self.areas[area.name] - min_off
            else:
                difference = -2

            if difference != -2:
                if (len(temp_list) == class_attr.areas_count) and (0 <= self.areas[area.name] < 4) and ((difference == 0) or (difference == -1)) and (self.budget >= class_attr.office_price):
                    self.budget -= class_attr.office_price
                    self.areas[area.name] += 1
                    print(f'На участке {self.name} {area.name} появился филиал ({self.areas[area.name]}). Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.areas}')
                elif len(temp_list) < class_attr.areas_count:
                    print(f'{self.name} не является монополистом данной отрасли, поэтому филиал установить невозможно')
                elif (self.areas[area.name] == 4) and (difference == 0):
                    print(f'На участок {area.name} следует установить не филиал, а предприятие')
                elif self.areas[area.name] == -1:
                    print(f'Участок {area.name} заложен, поэтому филиал установить невозможно')
                elif (difference > 0) and (len(temp_list) == class_attr.areas_count):
                    print(f'{self.name} не может установить филиал на участок {area.name}, потому что предварительно следует установить филиалы на другие участки отрасли')
            else:
                print(f'{self.name} не является монополистом данной отрасли, поэтому филиал установить невозможно')
        else: print(f'{area.name} нет в списке участков игрока {self.name}')

    # Продажа филиалов
    def sale_office(self, area):
        class_name = type(area).__name__
        class_attr = getattr(self, class_name, None)
        if area.name in self.areas:
            temp_list2 = []
            for k in self.areas:
                if (k in class_attr.areas_list) and (k != area.name):
                    temp_list2.append(self.areas[k])
            if temp_list2:
                min_off = max(temp_list2)
                difference = self.areas[area.name] - min_off
            else: difference = -2

            if difference != -2:
                if (0 < self.areas[area.name] <= 4) and ((difference == 0) or (difference == 1)):
                    self.budget += 0.5*class_attr.office_price
                    self.areas[area.name] -= 1
                    if self.areas[area.name] == 0:
                        print(f'{self.name} продал филиал на участке {area.name} за полцены - на участке больше нет филиалов. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.areas}')
                    else:
                        print(f'{self.name} продал филиал на участке {area.name} за полцены. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.areas}')
                elif self.areas[area.name] == 0:
                    print(f'На участке {area.name} игрока {self.name} нет филиалов. Продажа не удалась')
                elif self.areas[area.name] == -1:
                    print(f'Участок {area.name} заложен игроком {self.name}. Продажа филиала не удалась')
                elif self.areas[area.name] == 5:
                    print(f'На участке{area.name} установлено предприятие, а не филиал - продажа филиала не удалась')
                elif difference == -1:
                    print(f'Есть участки в отрасли {class_attr.name}, на которых расположено предприятие или больше филиалов, чем на данном. Игроку {self.name} не удалось продать филиал на учатстке {area.name}')
            else:
                print(f'Продажа офиса игроком {self.name} при данных обстоятельствах невозможна')
        else: 
            print(f'{area.name} нет в списке участков игрока {self.name}')

    # Покупка предприятия
    def get_firm(self, area):
        class_name = type(area).__name__
        class_attr = getattr(self, class_name, None)

        temp_list = []
        for uchastok in self.areas:
            if uchastok in class_attr.areas_list:
                temp_list.append(uchastok)

        if area.name in self.areas:
            temp_list2 = []
            for k in self.areas:
                if (k in class_attr.areas_list) and (k != area.name):
                    temp_list2.append(self.areas[k])
            if temp_list2:
                min_off = max(temp_list2)
                difference = self.areas[area.name] - min_off
            else:
                difference = -2

            if difference != 2:
                if (self.areas[area.name] == 4) and ((difference == 0)or (difference == -1)) and (self.budget >= class_attr.firm_price):
                    self.budget -= class_attr.firm_price
                    self.areas[area.name] = 5
                    print(f'{self.name} приобрел предприятие ({self.areas[area.name]}) для участка {area.name}. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.areas}')
                elif 0 <= self.areas[area.name] < 4:
                    print(f'Прежде, чем установить предприятие на участок {area.name}, игроку {self.name} следует установить филиал. Предприятие не установлено')
                elif self.areas[area.name] == -1:
                    print(f'Участок {area.name} игрока {self.name} заложен. Предприятие не установлено')
                elif (difference > 0) and (len(temp_list) == class_attr.areas_count):
                    print(f'Предприятие уже установлено на участке {area.name}. Но есть возможность установить предприятие(-я) на другие участки отрасли {class_attr.name}')
                elif self.budget < class_attr.firm_price:
                    print(f'Игроку {self.name} не хватает денег. Предприятие на участке {area.name} не установлено')
                elif (self.areas[area.name] == 5) and (difference == 0):
                    print(f'Предприятие на участке {area.name} игрока {self.name} уже установлено, как и предприятия на всех прочих участках отрасли {class_attr.name}')
            else:
                print(f'Покупка предприятия игроком {self.name} при данных обстоятельствах невозможна')
        else: 
            print(f'Участка {area.name} нет в собственности у {self.name}. Предприятие не установлено')

    # Продажа предприятия
    def sale_firm(self, area):
        class_name = type(area).__name__
        class_attr = getattr(self, class_name, None)
        if area.name in self.areas:
            temp_list2 = []
            for k in self.areas:
                if (k in class_attr.areas_list) and (k != area.name):
                    temp_list2.append(self.areas[k])
            if temp_list2:
                min_off = max(temp_list2)
                difference = self.areas[area.name] - min_off
            else: difference = -2

            if difference != -2:
                if (self.areas[area.name] == 5) and ((difference == 0) or (difference == 1)):
                    self.budget += 0.5*class_attr.firm_price
                    self.areas[area.name] = 4
                    print(f'Предприятие на участке {area.name} продано игроком {self.name} за полцены. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.areas}')
                elif 0 < self.areas[area.name] < 5:
                    print(f'На участке {area.name} игрока {self.name} и так нет предприятия, но установлены филиалы. Следует продать их')
                elif self.areas[area.name] == 0:
                    print(f'На участке {area.name} игрока {self.name} нет филиалов и предприятий. Продажа не удалась')
                elif self.areas[area.name] == -1: 
                    print(f'Участок {area.name} заложен игроком {self.name}. Продажа предприятия не удалась')
            else:
                print(f'Продажа предприятия игроком {self.name} при данных обстоятельствах невозможна')
        else:
            print(f'Участка {area.name} нет в собственности у {self.name}. Предприятие не продано')

    # Оплата аренды
    def pay_area_rent(self, area):
        if area.owner != self:
            try:
                if area.owner.areas[area.name] == 0:
                    price = area.rent_stock
                elif area.owner.areas[area.name] == 1:
                    price = area.rent_one_off
                elif area.owner.areas[area.name] == 2:
                    price = area.rent_two_off
                elif area.owner.areas[area.name] == 3:
                    price = area.rent_three_off
                elif area.owner.areas[area.name] == 4:
                    price = area.rent_four_off
                elif area.owner.areas[area.name] == 5:
                    price = area.rent_firm
            except AttributeError:
                pass
            
            if (area.owner != '') and (area.owner.areas[area.name] > -1) and (self.budget >= price):
                print(f'Бюджет {area.owner.name} был равен {area.owner.budget}')
                print(f'Бюджет {self.name} был равен {self.budget}')
                self.budget -= price
                area.owner.budget += price
                print(f'Бюджет {area.owner.name} стал равен {area.owner.budget}')
                print(f'Бюджет {self.name} стал равен {self.budget}')
            elif area.name in User.areas_list:
                print(f'Участок {area.name} еще никем не куплен, аренду платить не за что')
            elif (area.owner.areas[area.name] > -1) and (self.budget < price):
                print(f'Игроку {self.name} не хватает денег, чтобы заплатить аренду за участок {area.name}')
            elif area.owner.areas[area.name] == -1:
                print(f'Участок {area.name} заложен игроком {area.owner.name}, поэтому {self.name} не должен платить аренду')
        else: print('Нет смысла платить аренду самому себе')

    # Передать участок/транспорт/помощника другому игроку
    def give_thing(self, thing, user):
        if user != self:
            if type(thing).__name__ == ('First_1' or 'First_2' or 'Second_1' or 'Second_2' or 'Third_1' or 'Third_2' or 'Fourth_1' or 'Fourth_2'):
                if (thing.name in self.areas) and (self.areas[thing.name] > -1):
                    user.areas[thing.name] = self.areas.pop(thing.name)
                    print(f'{self.name} передал участок игроку {user.name}.\nВ собственности у {self.name}: {self.areas}\nВ собственности у {user.name}: {user.areas}')
                elif (thing.name in self.areas) and (self.areas[thing.name] == -1):
                    print(f'Участок {thing.name} игрока {self.name} заложен, поэтому не может быть передан')
                elif thing.name not in self.areas:
                    print(f'Участок {thing.name} не принадлежит {self.name}, поэтому не может быть передан')
            elif type(thing).__name__ == 'Transport':
                if (thing.name in self.transps) and (self.transps[thing.name] > -1):
                    user.transps[thing.name] = self.transps.pop(thing.name)
                    print(f'{self.name} передал транспорт {thing.name} игроку {user.name}.\nВ собственности у {self.name}: {self.transps}\nВ собственности у {user.name}: {user.transps}')
                elif (thing.name in self.transps) and (self.transps[thing.name] == -1):
                    print(f'Участок {thing.name} игрока {self.name} заложен, поэтому не может быть передан')
                elif thing.name not in self.transps:
                    print(f'Транспорт {thing.name} не принадлежит {self.name}, поэтому не может быть передан')
            elif type(thing).__name__ == 'Support':
                if (thing.name in self.sups) and (self.sups[thing.name] > -1):
                    user.sups[thing.name] = self.sups.pop(thing.name)
                    print(f'{self.name} передал помощника {thing.name} игроку {user.name}.\nВ собственности у {self.name}: {self.sups}\nВ собственности у {user.name}: {user.sups}')
                elif (thing.name in self.sups) and (self.sups[thing.name] == -1):
                    print(f'Помощник {thing.name} игрока {self.name} под залогом, поэтому не может быть передан')
                elif thing.name not in self.sups:
                    print(f'Помощник {thing.name} не принадлежит {self.name}, поэтому не может быть передан')
        else: print(f'Нельзя передать собственность самому себе')
    
    # Передать деньги другому игроку
    def give_money(self, money: int, user):
        try:
            if money >= 1:
                if (self.budget >= money) and (self != user):
                    print(f'Бюджет {self.name} ДО передачи денег: {self.budget}')
                    print(f'Бюджет {user.name} ДО получения денег: {user.budget}')
                    user.budget += money
                    self.budget -= money
                    print(f'Бюджет {self.name} ПОСЛЕ передачи денег: {self.budget}')
                    print(f'Бюджет {user.name} ПОСЛЕ получения денег: {user.budget}')
                elif self == user:
                    print('Нет смысла передавать деньги самому себе')
                elif self.budget < money:
                    print(f'{self.name} не может передать игроку {user.name} {money} галлеонов, потому что у него их нет')
            else:
                print('Нет смысла передавать нулевую сумму')
        except TypeError: print('Надо ввести сумму в формате int')

    # Покупка транспорта
    def buy_transport(self, transp):
        if (transp.name in User.transport_list) and (self.budget >= 200):
            print(f'Общий список средств передвижения ДО приобретения: {User.transport_list}')
            self.budget -= 200
            User.del_area_from_gen_list(transp)
            self.transps[transp.name] = 0
            transp.owner = self
            print(f'Общий список средств передвижения ПОСЛЕ приобретения: {User.transport_list}')
            print(f"Игроку {self.name} добавлен транспорт {transp.name}. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.transps}")
        elif (transp.name in self.transps) and (self.transps[transp.name] == 0):
            print(f'{transp.name} уже принадлежит игроку {self.name} и не может быть куплен повторно')
        elif (transp.name in self.transps) and (self.transps[transp.name] == -1):
            print(f'{self.name} ранее заложил этот транспорт, и приобрести его этим методом нельзя')
        elif (transp.name not in User.transport_list) and (transp.name not in self.transps):
            print(f"Транспорта {transp.name} уже нет в общем списке участков, и {self.name} не может его купить. Он находится в собственности {transp.owner.name}")
        elif (transp.name in User.transport_list) and (transp.name not in self.transps) and (self.budget < 200):
            print(f"Стоимость транспорта '{transp.name}' слишком велика")

    # Заложение транспорта
    def dep_transp(self, transp):
        if (transp.name in self.transps) and (self.transps[transp.name] == 0):
            self.transps[transp.name] = -1
            self.budget += 100
            print(f'Игрок {self.name} заложил {transp.name}. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.transps}')
        elif (transp.name in self.transps) and (self.transps[transp.name] == -1):
            print(f'{self.name} не удалось заложить {transp.name} - он у него уже заложен')
        elif (transp.name not in self.transps) and (transp.name in User.transport_list):
            print(f'{transp.name} прежде следует купить, а только потом закладывать. Транспорт не заложен')
        elif (transp.name not in self.transps) and (transp.name not in User.transport_list):
            print(f'Игрок {self.name} не может заложить транспорт, находящийся в собственности другого игрока. {transp.name} принадлежит {transp.owner.name}')

    # Выкуп заложенного транспорта
    def get_dep_transp(self, transp):
        if (transp.name in self.transps) and (self.transps[transp.name] == -1) and (self.budget >= 110):
            self.transps[transp.name] = 0
            self.budget -= 110
            print(f'{self.name} выкупил заложенный транспорт {transp.name}. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.transps}')
        elif transp.name not in self.transps:
            print(f'Транспорт {transp.name} не принадлежит {self.name}')
        elif self.transps[transp.name] == 0:
            print(f'{self.name} уже имеет {transp.name} в собственности, транспорт не под залогом')
        elif (transp.name in self.transps) and (self.transps[transp.name] == -1) and (self.budget < 110):
            print(f'{self.name} не может выкупить {transp.name} из залога, потому что в его бюджете недостаточно средств')

    # Оплатить аренду за использование транспорта
    def pay_transp_rent(self, transp):
        if transp.owner != self:
            try:
                if len(transp.owner.transps) == 1:
                    price = 25
                elif len(transp.owner.transps) == 2:
                    price = 50
                elif len(transp.owner.transps) == 3:
                    price = 100
                elif len(transp.owner.transps) == 4:
                    price = 200
            except AttributeError:
                pass
            
            if (transp.owner != '') and (transp.owner.transps[transp.name] > -1) and (self.budget >= price):
                print(f'Бюджет {transp.owner.name} был равен {transp.owner.budget}')
                print(f'Бюджет {self.name} был равен {self.budget}')
                self.budget -= price
                transp.owner.budget += price
                print(f'Бюджет {transp.owner.name} стал равен {transp.owner.budget}')
                print(f'Бюджет {self.name} стал равен {self.budget}')
            elif transp.name in User.transport_list:
                print(f'Транспорт {transp.name} еще никем не куплен, аренду платить не за что')
            elif (transp.owner.areas[transp.name] == 0) and (self.budget < price):
                print(f'Игроку {self.name} не хватает денег, чтобы заплатить аренду за использование транспорта {transp.name}')
            elif transp.owner.areas[transp.name] == -1:
                print(f'Транспорт {transp.name} заложен игроком {transp.owner.name}, поэтому {self.name} не должен платить аренду за его использование')
        else: print('Нет смысла платить аренду самому себе')

    # Покупка саппорта
    def buy_support(self, sup):
        if (sup.name in User.support_list) and (self.budget >= 150):
            print(f'Общий список средств передвижения ДО приобретения: {User.support_list}')
            self.budget -= 150
            User.del_area_from_gen_list(sup)
            self.sups[sup.name] = 0
            sup.owner = self
            print(f'Общий список средств передвижения ПОСЛЕ приобретения: {User.support_list}')
            print(f"Игроку {self.name} добавлен помощник {sup.name}. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.sups}")
        elif (sup.name in self.sups) and (self.sups[sup.name] == 0):
            print(f'{sup.name} уже принадлежит игроку {self.name} и не может быть куплен повторно')
        elif (sup.name in self.sups) and (self.sups[sup.name] == -1):
            print(f'{self.name} ранее отдал этого помощника под залог, и приобрести его этим методом нельзя')
        elif (sup.name not in User.support_list_list) and (sup.name not in self.sups):
            print(f"Помощника {sup.name} уже нет в общем списке участков, и {self.name} не может его купить. Он находится в собственности {sup.owner.name}")
        elif (sup.name in User.transport_list) and (sup.name not in self.transps) and (self.budget < 150):
            print(f"Стоимость помощника '{sup.name}' слишком велика") 

    # Заложение саппорта
    def dep_sup(self, sup):
        if (sup.name in self.sups) and (self.sups[sup.name] == 0):
            self.sups[sup.name] = -1
            self.budget += 75
            print(f'Игрок {self.name} отдал под залог помощника {sup.name}. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.sups}')
        elif (sup.name in self.sups) and (self.sups[sup.name] == -1):
            print(f'{self.name} не удалось отдать под залог {sup.name} - он у него уже под залогом')
        elif (sup.name not in self.sups) and (sup.name in User.support_list):
            print(f'{sup.name} прежде следует купить, а только потом закладывать. Помощник не заложен')
        elif (sup.name not in self.sups) and (sup.name not in User.support_list):
            print(f'Игрок {self.name} не может заложить помощника, находящегося в собственности другого игрока. {sup.name} принадлежит {sup.owner.name}')

    # Выкуп заложенного саппорта
    def get_dep_sup(self, sup):
        if (sup.name in self.sups) and (self.sups[sup.name] == -1) and (self.budget >= 83):
            self.sups[sup.name] = 0
            self.budget -= 83
            print(f'{self.name} выкупил помощника {sup.name} из залога. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.sups}')
        elif sup.name not in self.sups:
            print(f'Помощник {sup.name} не принадлежит {self.name}')
        elif self.sups[sup.name] == 0:
            print(f'{self.name} уже имеет {sup.name} в собственности, помощник не под залогом')
        elif (sup.name in self.sups) and (self.sups[sup.name] == -1) and (self.budget < 83):
            print(f'{self.name} не может выкупить {sup.name} из залога, потому что в его бюджете недостаточно средств')

    # Оплата за использование помощника
    def pay_sup_rent(self, sup):
        try:
            if self != sup.owner:
                if (len(sup.owner.sups) == 2) and (sup.owner.sups[sup.name] > -1):
                    r1 = randint(1, 6)
                    r2 = randint(1, 6)
                    price = 10*(r1+r2)
                    print(f'На костях выпало {r1} и {r2}. У {sup.owner.name} два помощника, поэтому результат умножается на 10 и равен {price}')
                    if self.budget >= price:
                        print(f'Бюджет {sup.owner.name} был равен {sup.owner.budget}')
                        print(f'Бюджет {self.name} был равен {self.budget}')
                        self.budget -= price
                        sup.owner.budget += price
                        print(f'Бюджет {sup.owner.name} стал равен {sup.owner.budget}')
                        print(f'Бюджет {self.name} стал равен {self.budget}')
                    else: print(f'У {self.name} недостаточно средств, чтобы заплатить за помощника игроку {sup.owner.name}')
                elif (len(sup.owner.sups) == 1) and (sup.owner.sups[sup.name] > -1):
                    r1 = randint(1, 6)
                    r2 = randint(1, 6)
                    price = 4*(r1+r2)
                    print(f'На костях выпало {r1} и {r2}. У {sup.owner.name} один помощник, поэтому результат умножается на 4 и равен {price}')
                    if self.budget >= price:
                        print(f'Бюджет {sup.owner.name} был равен {sup.owner.budget}')
                        print(f'Бюджет {self.name} был равен {self.budget}')
                        self.budget -= price
                        sup.owner.budget += price
                        print(f'Бюджет {sup.owner.name} стал равен {sup.owner.budget}')
                        print(f'Бюджет {self.name} стал равен {self.budget}')
                    else: print(f'У {self.name} недостаточно средств, чтобы заплатить за помощника игроку {sup.owner.name}')
                elif sup.owner.sups[sup.name] == -1:
                    print(f'{sup.owner.name} отдал своего помощника {sup.name} под залог, поэтому {self.name} не обязан платить')
            else: print(f'Нет смысла платить аренду самому себе')
        except AttributeError:
            print(f'У {sup.name} нет хозяина')

    # Покупка вещи за свободную сумму на аукционе
    def buy_thing_in_auction(self, thing, price):
        if (thing.name in (User.areas_list or User.transport_list or User.support_list)) and (self.budget >= price):
            self.budget -= price
            User.del_area_from_gen_list(thing)
            if type(thing).__name__ == ('First_1' or 'First_2' or 'Second_1' or 'Second_2' or 'Third_1' or 'Third_2' or 'Fourth_1' or 'Fourth_2'):
                self.areas[thing.name] = 0
                print(f'Продано! {self.name} приобрел участок {thing.name} за {price} галлеонов')
            elif type(thing).__name__ == 'Transport':
                self.transps[thing.name] = 0
                print(f'Продано! {self.name} приобрел транспорт {thing.name} за {price} галлеонов')
            elif type(thing).__name__ == 'Support':
                self.sups[thing.name] = 0
                print(f'Продано! {self.name} приобрел помощника {thing.name} за {price} галлеонов')
        elif thing.name not in (User.areas_list or User.transport_list or User.support_list):
            print(f'{thing.name} нет на поле - разыгрывать на аукционе нечего')
        elif (thing.name in (User.areas_list or User.transport_list or User.support_list)) and (self.budget < price):
            print(f'{self.name} не может приобрести лот на сумму {price}, потому что у него нет таких денег')
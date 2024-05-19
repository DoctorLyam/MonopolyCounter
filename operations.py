from area import Area, First_1, First_1_son, First_2, First_2_son, Transport

# Статусы участков:
# -1 - заложен; 0 - куплен; 1,2,3,4 - установлен(-ы) филиал(-ы); 5 - установлено предприятие 

class User(Area):
    areas_list = ['Дом Гарри', 'Вокзал Кингс-Кросс', 'Отдел магического транспорта', 'Отдел тайн', 'Отдел обеспечения магического правопорядка']
    transport_list = ['Хогвартс-Экспресс', 'Летающая метла', 'Летучий порох', 'Магический портал']

    def __init__(self, name, areas, transps, supports, budget: int, bolshoy_dyadya=[]):
        self.name = name
        self.areas = areas
        self.transps = transps
        self.supports = supports
        self.budget = budget
        self.bolshoy_dyadya = bolshoy_dyadya
        self.First_1 = First_1_son()
        self.First_2 = First_2_son()

    # Удаление участка из общего списка участков
    @classmethod
    def del_area_from_Areas(cls, area_name):
        return cls.areas_list.remove(area_name)
    
    @classmethod
    def del_transport_from_Transports(cls, transport_name):
        return cls.transport_list.remove(transport_name)

    # Взять деньги из банка
    def get_money_from_bank(self, money: int):
        try:
            self.budget += money
            print(f'{self.name} получил {money} галлеонов из банка.\nБюджет {self.name} составляет {self.budget}')
        except TypeError:
            print('Сумма получаемых в банке денег должна быть в формате int')

    def give_money_to_bank(self, money: int):
        try:
            self.budget -= money
            print(f'{self.name} отдал {money} галлеонов банку.\nБюджет {self.name} составляет {self.budget}')
        except TypeError:
            print('Сумма отдаваемы банку денег должна быть в формате int')

    # Круговой доход
    def cicle_add(self):
        self.budget += 200
        print(f'Получен круговой доход. Бюджет {self.name} равен {self.budget}')

    # Налог
    def nalog(self):
        if self.budget >= 50:
            self.budget -= 50
            print(f'{self.name} платит за выход из тюрьмы. Бюджет {self.name} равен {self.budget}')
        else: print(f'{self.name} недостаточно денег для выхода на свободу')
    
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
            User.del_area_from_Areas(area.name)
            print(f'Общий спиcок предприятий ПОСЛЕ приобретения: {User.areas_list}')
            self.areas[area.name] = 0
            self.budget -= brown_one.price
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

    # Покупка заложенного участка
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
            else: difference == -2

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
                difference == -2

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
            else: difference == -2

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
    def pay_rent(self, area):
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
        
        if (area.name not in User.areas_list) and (area.owner.areas[area.name] > -1) and (self.budget >= price):
            print(f'Бюджет {area.owner.name} был равен {area.owner.budget}')
            print(f'Бюджет {self.name} был равен {self.budget}')
            self.budget -= price
            area.owner.budget += price
            print(f'Бюджет {area.owner.name} стал равен {area.owner.budget}')
            print(f'Бюджет {self.name} стал равен {self.budget}')
    
    # Передать участок другому игроку
    def give_area(self, area, user):
        if (area.name in self.areas) and (self.areas[area.name] > -1):
            user.areas[area.name] = self.areas.pop(area.name)
            print(f'{self.name} передал участок игроку {user.name}.\nВ собственности у {self.name}: {self.areas}\nВ собственности у {user.name}: {user.areas}')
        elif (area.name in self.areas) and (self.areas[area.name] == -1):
            print(f'Участок {area.name} игрока {self.name} заложен, поэтому не может быть передан')
        elif area.name not in self.areas:
            print(f'Участок {area.name} не принадлежит {self.name}, поэтому не может быть передан')
    
    # Передать деньги другому игроку
    def give_money(self, money: int, user):
        try:
            if self.budget >= money:
                print(f'Бюджет {self.name} ДО передачи денег: {self.budget}')
                print(f'Бюджет {user.name} ДО получения денег: {user.budget}')
                user.budget += money
                self.budget -= money
                print(f'Бюджет {self.name} ПОСЛЕ передачи денег: {self.budget}')
                print(f'Бюджет {user.name} ПОСЛЕ получения денег: {user.budget}')
            else:
                print(f'{self.name} не может передать игроку {user.name} {money} галлеонов, потому что у него их нет')
        except TypeError: print('Надо ввести сумму в формате int')

    # Покупка транспорта
    def buy_transport(self, transp):
        if (transp.name in User.transport_list) and (self.budget >= 200):
            print(f'Общий список средств передвижения ДО приобретения: {User.transport_list}')
            self.budget -= 200
            User.del_transport_from_Transports(transp.name)
            self.transps[transp.name] = 0
            transp.owner = self
            print(f'Общий список средств передвижения ДО приобретения: {User.transport_list}')
            print(f"Игроку {self.name} добавлен участок {transp.name}. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.transps}")
        elif (transp.name in self.transps) and (self.transps[transp.name] == 0):
            print(f'{transp.name} уже принадлежит игроку {self.name} и не может быть куплен повторно')
        elif (transp.name in self.transps) and (self.transps[transp.name] == -1):
            print(f'{self.name} ранее заложил этот транспорт, и приобрести его этим методом нельзя')
        elif (transp.name not in User.transport_list) and (transp.name not in self.transps):
            print(f"Транспорта {transp.name} уже нет в общем списке участков, и {self.name} не может его купить. Он находится в собственности {transp.owner.name}")
        elif (transp.name in User.transport_list) and (transp.name not in self.transps) and (self.budget < 200):
            print(f"Стоимость транспорта '{transp.name}' слишком велика")

    # Покупка заложенного транспорта
    def get_dep_transp(self, transp):
        if (transp.name in self.areas) and (self.areas[transp.name] == -1) and (self.budget >= 110):
            self.areas[transp.name] = 0
            self.budget -= 110
            print(f'{self.name} выкупил заложенный участок. Баланс {self.name} равен {self.budget}.\nВ собственности {self.name} находятся: {self.transps}')
        elif transp.name not in self.areas:
            print(f'Транспорт {transp.name} не принадлежит {self.name}')
        elif self.areas[transp.name] == 0:
            print(f'{self.name} уже имеет {transp.name} в собственности, транспорт не под залогом')
        elif (transp.name in self.areas) and (self.areas[transp.name] == -1) and (self.budget < 110):
            print(f'{self.name} не может выкупить {transp.name} из залога, потому что в его бюджете недостаточно средств')


user_1 = User(name="Саша", areas={}, transps={}, supports={}, budget=2000)
user_2 = User(name="Настя", areas={}, transps={}, supports={}, budget=2000)

transp_one = Transport(name='Хогвартс-Экспресс')
transp_two = Transport(name='Летающая метла')
transp_three = Transport(name='Летучий порох')
transp_four = Transport(name='Магический портал')

brown_one = First_1(name='Дом Гарри', price=60, deposite=30, rent_stock=2, 
            rent_one_off=10, rent_two_off=30, rent_three_off=90, rent_four_off=160, rent_firm=250)
brown_two = First_1(name='Вокзал Кингс-Кросс', price=60, deposite=30, rent_stock=4, 
            rent_one_off=20, rent_two_off=60, rent_three_off=180, rent_four_off=320, rent_firm=450)
blue_one = First_2(name='Отдел магического транспорта', price=100, deposite=50, rent_stock=6, 
            rent_one_off=30, rent_two_off=90, rent_three_off=270, rent_four_off=400, rent_firm=550)
blue_two = First_2(name='Отдел тайн', price=100, deposite=50, rent_stock=6, 
            rent_one_off=30, rent_two_off=90, rent_three_off=270, rent_four_off=400, rent_firm=550)
blue_three = First_2(name='Отдел обеспечения магического правопорядка', price=120, deposite=60, rent_stock=8, 
            rent_one_off=40, rent_two_off=100, rent_three_off=300, rent_four_off=450, rent_firm=600)

user_1.buy_transport(transp_one)
user_1.buy_transport(transp_one)
user_2.buy_transport(transp_one)


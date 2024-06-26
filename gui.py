# Написание графического интерфейса для программы
from area import Area, Transport, Support, First_1, First_1_son, First_2, First_2_son, Second_1, Second_1_son, Second_2, Second_2_son, Third_1, Third_1_son, Third_2, Third_2_son, Fourth_1, Fourth_1_son, Fourth_2, Fourth_2_son
from operations import User
import tkinter as tk
from tkinter import ttk

user_1 = User(name="Саша", areas={}, transps={}, sups={}, budget=2000)
user_2 = User(name="Настя", areas={}, transps={}, sups={}, budget=2000)

transp_one = Transport(name='Хогвартс-Экспресс')
transp_two = Transport(name='Летающая метла')
transp_three = Transport(name='Летучий порох')
transp_four = Transport(name='Магический портал')

sup_one = Support(name='Добби')
sup_two = Support(name='Кикимер')

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

pink_one = Second_1(name='Магазин Совы', price=140, deposite=70, rent_stock=10,
                    rent_one_off=50, rent_two_off=150, rent_three_off=450, rent_four_off=625, rent_firm=750)
pink_two = Second_1(name='Лавка Олливандера', price=140, deposite=70, rent_stock=10,
                    rent_one_off=50, rent_two_off=150, rent_three_off=450, rent_four_off=625, rent_firm=750)
pink_three = Second_1(name='Всё для Квиддича', price=160, deposite=80, rent_stock=12,
                    rent_one_off=60, rent_two_off=180, rent_three_off=500, rent_four_off=700, rent_firm=900)

orange_one = Second_2(name='Три метлы', price=180, deposite=90, rent_stock=14,
            rent_one_off=70, rent_two_off=200, rent_three_off=550, rent_four_off=750, rent_firm=950)
orange_two = Second_2(name='Кабанья голова', price=180, deposite=90, rent_stock=14,
            rent_one_off=70, rent_two_off=200, rent_three_off=550, rent_four_off=750, rent_firm=950)
orange_three = Second_2(name='Сладкое королевство', price=200, deposite=100, rent_stock=16,
            rent_one_off=80, rent_two_off=220, rent_three_off=600, rent_four_off=800, rent_firm=1000)

red_one = Third_1(name='Большой зал', price=220, deposite=110, rent_stock=18,
        rent_one_off=90, rent_two_off=250, rent_three_off=700, rent_four_off=875, rent_firm=1050)
red_two = Third_1(name='Выручай Комната', price=220, deposite=110, rent_stock=18,
        rent_one_off=90, rent_two_off=250, rent_three_off=700, rent_four_off=875, rent_firm=1050)
red_three = Third_1(name='Хижина Хагрида', price=240, deposite=120, rent_stock=20,
        rent_one_off=100, rent_two_off=300, rent_three_off=750, rent_four_off=925, rent_firm=1100)

yellow_one = Third_2(name='Карта Мародёров', price=260, deposite=130, rent_stock=22,
        rent_one_off=110, rent_two_off=330, rent_three_off=800, rent_four_off=975, rent_firm=1150)
yellow_two = Third_2(name='Маховик времени', price=260, deposite=130, rent_stock=22,
        rent_one_off=110, rent_two_off=330, rent_three_off=800, rent_four_off=975, rent_firm=1150)
yellow_three = Third_2(name='Меч Гриффиндора', price=280, deposite=140, rent_stock=24,
        rent_one_off=120, rent_two_off=360, rent_three_off=850, rent_four_off=1025, rent_firm=1200)

green_one = Fourth_1(name='Бузинная палочка', price=300, deposite=150, rent_stock=26,
        rent_one_off=130, rent_two_off=390, rent_three_off=900, rent_four_off=1100, rent_firm=1275)
green_two = Fourth_1(name='Воскрешающий камень', price=300, deposite=150, rent_stock=26,
        rent_one_off=130, rent_two_off=390, rent_three_off=900, rent_four_off=1100, rent_firm=1275)
green_three = Fourth_1(name='Мантия-Невидимка', price=320, deposite=160, rent_stock=28,
        rent_one_off=150, rent_two_off=450, rent_three_off=1000, rent_four_off=1200, rent_firm=1400)

purple_one = Fourth_2(name='Придира', price=350, deposite=175, rent_stock=35,
        rent_one_off=175, rent_two_off=500, rent_three_off=1100, rent_four_off=1500, rent_firm=1800)
purple_two = Fourth_2(name='Ежедневный пророк', price=400, deposite=200, rent_stock=50,
        rent_one_off=175, rent_two_off=500, rent_three_off=1100, rent_four_off=1500, rent_firm=1800)

# Примеры запуска кода:
# user_1.give_thing(transp_one, user_2) # positive
# user_2.buy_area(purple_one) # negative
# user_1.get_office(purple_two) # negative
# user_1.get_office(purple_one) # positive

#-----------------------------------------------------------------------------
root = tk.Tk()
root.title('Счетчик для Монополии')
root.geometry("1000x700") # Размеры окна
root.minsize(1000,500)   # минимальные размеры: ширина - 200, высота - 150
label = tk.Label(text='Монополия') # Текстовая метка
label.pack() # Размещение текстовой метки в окне
# root.iconbitmap(default="ICO.ico") # Иконка
# WM_DELETE_WINDOW — это событие в системе управления окнами, которое указывает, что пользователь хочет закрыть окно
# protocol() позволяет переопределить событие
# и в данном случае мы биндим на это событие корректное закрытие всего приложения destroy (чтоб наверняка) 
def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения...")
root.protocol("WM_DELETE_WINDOW", finish)
root.attributes("-alpha", 0.95) # Прозрачность


# def log_message(message):
#     # Добавляем новое сообщение в конец текстового поля
#     game_log.insert(tk.END, message + '\n')
#     # Прокручиваем текстовое поле до конца, чтобы видеть последние добавленные сообщения
#     game_log.see(tk.END)
# game_log = tk.Text(root, height=20, width=50)
# game_log.pack(side=tk.BOTTOM, anchor='ne', expand=True)
# log_message("Начало работы приложения")
# log_message("Загрузка данных...")
# log_message("Данные загружены успешно")

# Радиобаттон для выбора юзера
chosen_user = tk.StringVar(value='Юзер не выбран') # Тип переменной, которая будет хранить в себе состояние виджета в value
user_list = {'Саша':'user_1', 'Настя':'user_2'}
for user in user_list:
    user_rad = tk.Radiobutton(root, text=user, variable=chosen_user, value=user_list[user]).pack(anchor=tk.W)

# Радиобаттон для выбора второго юзера
chosen_user_2 = tk.StringVar(value='Юзер не выбран') # Тип переменной, которая будет хранить в себе состояние виджета в value
for user in user_list:
    user_rad = tk.Radiobutton(root, text=user, variable=chosen_user_2, value=user_list[user]).pack(anchor=tk.W)


# Поле для ввода числа
entry_text = tk.StringVar() # Вводимый текст
# само поле
sum = ttk.Entry(width=7, textvariable = entry_text).pack(anchor='nw', padx=8, pady=8)
def character_limit(entry_text):
        try:
                entry_text_1 = int(entry_text.get())
                if len(entry_text.get()) > 6:
                        entry_text.set(entry_text.get()[:-1])
        except ValueError:
              entry_text.set(entry_text.get()[:-1])
entry_text.trace("w", lambda *args: character_limit(entry_text))


# Список со словарями участков, транспорта и саппортов
all_things = [{'Дом Гарри':'brown_one', 'Вокзал Кингс-Кросс':'brown_two', 'Отдел магического транспорта':'blue_one', 'Отдел тайн':'blue_two', 
                'Отдел обеспечения магического правопорядка':'blue_three', 'Магазин Совы':'pink_one', 'Лавка Олливандера':'pink_two', 'Всё для Квиддича':'pink_three',
                'Три метлы':'orange_one', 'Кабанья голова':'orange_two', 'Сладкое королевство':'orange_three', 
                'Большой зал':'red_one', 'Выручай Комната':'red_two', 'Хижина Хагрида':'red_three', 
                'Карта Мародёров':'yellow_one', 'Маховик времени':'yellow_two', 'Меч Гриффиндора':'yellow_three', 
                'Бузинная палочка':'green_one', 'Воскрешающий камень':'green_two', 'Мантия-Невидимка':'green_three', 
                'Придира':'purple_one', 'Ежедневный пророк':'purple_two'},
                {'Хогвартс-Экспресс':'transp_one','Летающая метла':'transp_two','Летучий порох':'transp_three', 'Магический портал':'transp_four'},
                {'Добби':'sup_one', 'Кикимер':'sup_two'}]

all_methods = {'Покупка участка':'buy_area', 'Заложение участка':'dep_area', 'Выкуп заложенного участка':'get_dep_area',
                'Покупка филиала':'get_office', 'Продажа филиала':'sale_office', 'Покупка предприятия':'get_firm', 'Продажа предприятия':'sale_firm',
                'Оплата аренды за использование участка':'pay_area_rent',
                
                'Покупка транспорта':'buy_transport', 'Заложение транспорта':'dep_transp',
                'Выкуп заложенного транспорта':'get_dep_transp', 'Оплата за использование чужого транспорта':'pay_transp_rent',
                
                'Покупка помощника':'buy_support', 'Заложить помощника':'dep_sup',
                'Выкуп заложенного помощника':'get_dep_sup', 'Оплата за использование чужого помощника':'pay_sup_rent',
                
                'Взять деньги из банка':'get_money_from_bank', 'Дать деньги банку':'give_money_to_bank',
                
                'Получить круговой доход':'cicle_add', 'Заплатить налог':'nalog', 'Выйти из тюрьмы':'prison',
                
                'Передать вещь другому игроку':'give_thing', 'Передать деньги другому игроку':'give_money',
                
                'Купить вещь за свободную сумму на аукционе':'buy_thing_in_auction'}

# Список выбора действий для участков
# Словарь с методами (действиями)
chosen_method = tk.StringVar(value='')
area_methods = ttk.Combobox(root, values=list(all_methods.keys()), textvariable=chosen_method, width=32).pack(anchor='w', padx=10, pady=10)

# Список выбора участка
chosen_area = tk.StringVar(value='')
areas = ttk.Combobox(root, values=list(all_things[0].keys()), textvariable=chosen_area).pack(anchor='nw', padx=6, pady=6)

# Список выбора транспорта
chosen_transp = tk.StringVar(value='')
transps = ttk.Combobox(root, values=list(all_things[1].keys()), textvariable=chosen_transp).pack(anchor='nw', padx=6, pady=6)

# Список выбора саппорта
chosen_sup = tk.StringVar(value='')
sups = ttk.Combobox(root, values=list(all_things[2].keys()), textvariable=chosen_sup).pack(anchor='nw', padx=6, pady=6)

#----------------------------------
# Функция для кнопки уникального действия над участком
def area_oper_btn():
        try:
                if chosen_method.get() in ('Покупка участка', 'Заложение участка', 'Выкуп заложенного участка',
                                           'Покупка филиала', 'Продажа филиала', 'Покупка предприятия',
                                           'Продажа предприятия', 'Оплата аренды за использование участка'):
                        exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'({all_things[0][chosen_area.get()]})')
                else:
                       print('Выберите уникальный метод для совершения действия над участком')
                       print(f'Выбран метод: {chosen_method.get()}')
        except SyntaxError:
              print('Выберите игрока')
        except KeyError:
              print('Выберите действие и/или вещь')
              

area_btn = ttk.Button(text="Совершить действие\nнад участком", command=area_oper_btn).pack(anchor='sw')
#----------------------------------
# Функция для кнопки уникального действия над транспортом
def transp_oper_btn():
        try:
                if chosen_method.get() in ('Покупка транспорта', 'Заложение транспорта',
                                        'Выкуп заложенного транспорта', 'Оплата за использование чужого транспорта'):
                        exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'({all_things[1][chosen_transp.get()]})')
                else:
                       print('Выберите уникальный метод для совершения действия над транспортом')
                       print(f'Выбран метод: {chosen_method.get()}')
        except SyntaxError:
              print('Выберите игрока')
        except KeyError:
              print('Выберите действие и/или вещь')

transp_btn = ttk.Button(text="Совершить действие\nнад транспортом", command=transp_oper_btn).pack(anchor='sw')
#----------------------------------
# Функция для кнопки уникального действия над саппортом
def sup_oper_btn():
        try:
                if chosen_method.get() in ('Покупка помощника', 'Заложить помощника',
                                        'Выкуп заложенного помощника', 'Оплата за использование чужого помощника'):
                        exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'({all_things[2][chosen_sup.get()]})')
                else:
                       print('Выберите уникальный метод для совершения действия над помощником')
                       print(f'Выбран метод: {chosen_method.get()}')
        except SyntaxError:
              print('Выберите игрока')
        except KeyError:
              print('Выберите действие и/или вещь')

sup_btn = ttk.Button(text="Совершить действие\nнад помощником", command=sup_oper_btn).pack(anchor='sw')
#----------------------------------
# Функция для взятия денег из банка
def give_money_to_bank():
        try:
                if chosen_method.get() == 'Взять деньги из банка':
                        exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'({entry_text.get()})')
                else:
                       print('Выберите метод "Взять деньги из банка"')
                                       
        except SyntaxError:
              print('Выберите игрока')
        except TypeError:
               print('Введите сумму для взятия из банка')

give_bank_btn = ttk.Button(text="Взять деньги из банка", command=give_money_to_bank).pack(anchor='sw')
#----------------------------------
# Функция, чтобы отдать деньги банку (МОЖНО УЙТИ В МИНУС - ИСПРАВИТЬ ЛОГИКУ)
def get_money_from_bank():
        try: 
                if chosen_method.get() == 'Дать деньги банку':
                     exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'({entry_text.get()})')
                else:
                       print('Выберите метод "Дать деньги банку"')
                                       
        except SyntaxError:
              print('Выберите игрока')
        except TypeError:
               print('Введите сумму, которую собираетесь дать банку')

get_bank_btn = ttk.Button(text="Дать деньги банку", command=get_money_from_bank).pack(anchor='sw')
#----------------------------------
# Функция для получения кругового дохода
def circle_add():
        try:
                if chosen_method.get() == 'Получить круговой доход':
                        exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'()')
                else:
                        print('Выберите метод "Получить круговой доход"')
        except SyntaxError:
              print('Выберите игрока')
circle_add_btn = ttk.Button(text="Получить круговой доход", command=circle_add).pack(anchor='sw')
#----------------------------------
# Функция уплаты налога
def nalog():
        try:
                if chosen_method.get() == 'Заплатить налог':
                        exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'()')
                else:
                        print('Выберите метод "Заплатить налог"')
        except SyntaxError:
              print('Выберите игрока')
nalog_btn = ttk.Button(text="Заплатить налог", command=nalog).pack(anchor='sw')
#----------------------------------
# Функция выхода из тюрьмы
def prison():
        try:
                if chosen_method.get() == 'Выйти из тюрьмы':
                     exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'()')
                else:
                     print('Выберите метод "Выйти из тюрьмы"')
        except SyntaxError:
              print('Выберите игрока')
prison_btn = ttk.Button(text="Выйти из тюрьмы", command=prison).pack(anchor='sw')
#---------------------------------
# Функция передачи участка другому игроку
def give_area():
        try:
                if chosen_method.get() == 'Передать вещь другому игроку':
                     exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'({all_things[0][chosen_area.get()]}, {chosen_user_2.get()})')
                else:
                     print('Выберите метод "Передать вещь другому игроку"')
        except SyntaxError:
              print('Выберите игрока')
        except KeyError:
              print(f'Выберите действие и/или участок')           
give_area_btn = ttk.Button(text="Дать участок другому игроку", command=give_area).pack(anchor='sw')
#---------------------------------
# Функция передачи транспорта другому игроку
def give_transp():
        try:
                if chosen_method.get() == 'Передать вещь другому игроку':
                     exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'({all_things[1][chosen_area.get()]}, {chosen_user_2.get()})')
                else:
                     print('Выберите метод "Передать вещь другому игроку"')
        except SyntaxError:
              print('Выберите игрока')
        except KeyError:
              print(f'Выберите действие и/или транспорт')           
give_transp_btn = ttk.Button(text="Дать транспорт другому игроку", command=give_transp).pack(anchor='sw')
#---------------------------------
# Функция передачи саппорта другому игроку
def give_sup():
        try:
                if chosen_method.get() == 'Передать вещь другому игроку':
                     exec(f'{chosen_user.get()}'+'.'+f'{all_methods[chosen_method.get()]}'+f'({all_things[2][chosen_area.get()]}, {chosen_user_2.get()})')
                else:
                     print('Выберите метод "Передать вещь другому игроку"')
        except SyntaxError:
              print('Выберите игрока')
        except KeyError:
              print('Выберите действие и/или помощника')           
give_sup_btn = ttk.Button(text="Дать помощника другому игроку", command=give_sup).pack(anchor='sw')



root.mainloop()

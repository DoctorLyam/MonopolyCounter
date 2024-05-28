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
# user_1.buy_area(purple_one) # positive
# user_2.buy_area(purple_one) # negative
# user_1.get_office(purple_two) # negative
# user_1.get_office(purple_one) # positive

#-----------------------------------------------------------------------------
root = tk.Tk()
root.title('Счетчик для Монополии')
root.geometry("1000x500") # Размеры окна
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


def log_message(message):
    # Добавляем новое сообщение в конец текстового поля
    game_log.insert(tk.END, message + '\n')
    # Прокручиваем текстовое поле до конца, чтобы видеть последние добавленные сообщения
    game_log.see(tk.END)
game_log = tk.Text(root, height=20, width=50)
game_log.pack(side=tk.BOTTOM, anchor='ne', expand=True)
log_message("Начало работы приложения")
log_message("Загрузка данных...")
log_message("Данные загружены успешно")

# Радиобаттон для выбора юзера
chosen_user = tk.IntVar(value=0) # Тип переменоой, которая будет хранить в себе состояние виджета в value
user_list = [user_1, user_2]
for numb, user in enumerate(user_list):
    tk.Radiobutton(root, text=user.name, variable=chosen_user, value=numb).pack(anchor=tk.W)

# Поле для ввода числа
entry_text = tk.StringVar() # Вводимый текст
# само поле
sum = ttk.Entry(width=10, textvariable = entry_text).pack(anchor='nw', padx=8, pady=8)
def character_limit(entry_text):
    if (len(entry_text.get())) > 5 and entry_text is int: #ИСПРАВИТЬ ЭТО УСЛОВИЕ
        entry_text.set(entry_text.get()[-1])
entry_text.trace("w", lambda *args: character_limit(entry_text))


# Список выбора участка
areas_list = [brown_one.name, brown_two.name, blue_one.name, blue_two.name, blue_three.name, pink_one.name, pink_two.name, pink_three.name,
             orange_one.name, orange_two.name, orange_three.name, red_one.name, red_two.name, red_three.name, yellow_one.name, yellow_two.name, yellow_three.name, 
             green_one.name, green_two.name, green_three.name, purple_one.name, purple_two.name]
areas = ttk.Combobox(root, values=areas_list).pack(anchor='nw', padx=6, pady=6)

# Список выбора действий
action_areas_list = []


# btn = ttk.Button(command=lambda:user_1.buy_area(brown_one), width=50)
# # Задам координаты кнопке
# btn.pack(anchor="nw")
# # устанавливаем параметр text
# btn["text"]="Send"



root.mainloop()

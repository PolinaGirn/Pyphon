text = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
        'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(text)):
    element = text[i].split(' ')

    name = element[-1].capitalize()
    print('Привет,', name)

# задание выполнено, вроде бы я не создавала отдельный список для имен
# новый список использовала только чтобы разделить строку
# чтобы вытащить из неё имя.

# вместо функции .capitalize() можно
# уменьшить все буквы и увеличить первую

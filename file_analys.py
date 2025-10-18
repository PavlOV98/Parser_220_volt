import os
from bs4 import BeautifulSoup
import json

from constants import save_dir

def add_if_exist(key, data, dict):
    if key in dict:
        data[key] = dict[key]
    else:
        data[key] = None


# Получаем список всех файлов и папок
all_items = os.listdir(save_dir)
print(all_items)

d = {'items':[]}
for file in all_items:
    # Открываем html файл для чтения, важно учесть кодировку
    with open(save_dir+file, 'r', encoding='windows-1251') as f:
        # Создаём объект BeautifulSoup
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')

        # Достаём имя по классу
        name = soup.select('.card-main-title')
        name = name[0].text.strip()

        # Достаём цену по классу, переводим в число
        price = soup.select('.card-lg-price')
        price = price[0].text.strip()
        price = price[:price.index('р.')]
        price = int(price.replace(' ', ''))

        # Достаём таблицу по тегу
        table = soup.find('table')
        # Из таблицы берём все строки
        table_content = table.find_all('tr')
        #print(table_content[0].text)

        print(name)
        #print(price)
        item = {'name':name, 'price':price}

        # Достаём из строк таблицы данные
        arr = {}
        for line in table_content:
            data = line.find_all('td')
            data[0] = data[0].text.strip()
            data[1] = data[1].text.strip()
            #print(data[0], data[1])
            arr[data[0]] = data[1]
        #print(arr)
        #print(table.text)

        # Выбираем нужные параметры
        keys = [
            'Вес', 'Напряжение аккумулятора (В)',
            'Макс. крутящий момент', 'Наличие удара',
            'Страна происхождения', 'Тип аккумулятора',
            'Аккумуляторов в комплекте', 'Количество скоростей',
            'Тип патрона', 'Емкость аккумулятора (Ач)'
        ]
        for key in keys:
            add_if_exist(key, item, arr)

        #print(item)
        # Добавляем данные в список
        d['items'].append(item.copy())

# Сохраняем данные в JSON файл
with open('out_file.json', 'w') as file:
    json.dump(d, file, indent=4)

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
d = {'items':[]}
print(all_items)
for file in all_items:
    with open(save_dir+file, 'r', encoding='windows-1251') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')

        name = soup.select('.card-main-title')
        name = name[0].text.strip()
        table = soup.find('table')
        table_content = table.find_all('tr')
        #print(table_content[0].text)
        price = soup.select('.card-lg-price')
        price = price[0].text.strip()

        print(name)
        #print(price)
        price = price[:price.index('р.')]
        price = int(price.replace(' ', ''))
        item = {'name':name, 'price':price}

        arr = {}
        for line in table_content:
            data = line.find_all('td')
            data[0] = data[0].text.strip()
            data[1] = data[1].text.strip()
            #print(data[0], data[1])
            arr[data[0]] = data[1]
        #print(arr)
        #print(table.text)
        keys = [
            'Вес', 'Напряжение аккумулятора (В)',
            'Макс. крутящий момент', 'Наличие удара',
            'Страна происхождения', 'Тип аккумулятора',
            'Аккумуляторов в комплекте', 'Количество скоростей',
            'Тип патрона', 'Емкость аккумулятора (Ач)'
        ]
        for key in keys:
            add_if_exist(key, item, arr)


        d['items'].append(item.copy())

with open('out_file.json', 'w') as file:
    json.dump(d, file, indent=4)

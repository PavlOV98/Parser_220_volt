import os
from bs4 import BeautifulSoup

from constants import save_dir

# Получаем список всех файлов и папок
all_items = os.listdir(save_dir)

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
        print(price)
        arr = []
        for line in table_content:
            data = line.find_all('td')
            data[0] = data[0].text.strip()
            data[1] = data[1].text.strip()
            #print(data[0], data[1])
            arr.append([data[0], data[1]])
        print(arr)
        #print(table.text)
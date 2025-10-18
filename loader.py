import requests
import time

# Импортируем константы из файла constants
# Это удобнее если они используются в нескольких файлах
# Плюс сами константы удобнее менять в отдельном файле
from constants import urls, url_beg, save_dir

urls_count = len(urls)
ind_len = len(str(urls_count))
for i, url in enumerate(urls):
    # Вывод для отслеживания прогресса
    print(f"file {i:{ind_len}d}/{urls_count} {url}")
    start_time = time.time()
    # Собираем ссылку на конкретный товар и делаем запрос
    response = requests.get(url_beg+url+'/')

    if response.status_code == 200:
        html_content = response.text
        file_name = save_dir+url+".html"
        with open(file_name, "w", encoding="windows-1251") as file:
            file.write(html_content)

        # Вычисление времени на загрузку страницы
        elapsed_time = time.time() - start_time
        print(f"file {i:{ind_len}d} finished time:{elapsed_time:.2f} sec")
    else:
        print("\033[31m"+f"error, code {response.status_code}"+"\033[0m")

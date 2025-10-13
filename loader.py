import requests

from constants import  urls, url_beg, save_dir

for url in urls:
    response = requests.get(url_beg+url+'/')
    if response.status_code == 200:
        html_content = response.text
        file_name = save_dir+url+".html"
        with open(file_name, "w", encoding="windows-1251") as file:
            file.write(html_content)

from page_loader.support_func import formatter, same_domain
import os
import requests
from bs4 import BeautifulSoup


def mat_downloader(html_way, file_name):
    # проверяем создана ли папка для файлов, если нет - создаем
    if not os.path.isdir(f'{html_way}/{file_name}_files'):
        os.mkdir(f'{html_way}/{file_name}_files')
    files = f'{html_way}/{file_name}_files'
    # открываем скаченный хтмл и создаем суп
    html_file = open(f'{html_way}/{file_name}.html')
    soup = BeautifulSoup(html_file, 'html.parser')
    for link in soup.find_all('a', 'link'):
        url = link.get('href')
        p = requests.get(url)
        # canonical - ссылки на саму себя, все равно записываем в files
        if link.get('rel') == "canonical":
            with open(f'{files}/{file_name}.html', 'w') as f:
                f.write(p.content)
                # заменяем линку в супе
                link['href'] = f'{files}/{file_name}.html'
        # если это css файл
        elif url[-4:] == '.css':
            css_name, css_extension = os.path.splitest(url)
            css_name = formatter(css_name)
            with open(f'{files}/{file_name}-{css_name}.css', 'w') as f:
                f.write(p.content)
                link['href'] = f'{files}/{file_name}-{css_name}.css'
        else:
            url_name = formatter(url)
            with open(f'{files}/{url_name}.html') as f:
                f.write(p.content)
                link['href'] = f'{files}/{url_name}.html'
            
mat_downloader('/home/ovechka/python-project-51/', 'ru-hexlet-io-courses')
from page_loader.support_func import formatter
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from cairosvg import svg2png
import io

current_dir = os.getcwd()

# принимает только расположение html и название файла без расширения


def img_downloader(html_way, file_name):
    # проверяем создана ли папка для файлов, если нет - создаем
    if not os.path.isdir(f'{html_way}/{file_name}_files'):
        os.mkdir(f'{html_way}/{file_name}_files')
    save_folder = f'{html_way}/{file_name}_files'
    # открываем ранее скачанный файл для супа
    html_file = open(f'{html_way}/{file_name}.html')
    soup = BeautifulSoup(html_file, 'html.parser')
    # тут получаем все ссылки с тегом img src
    for link in soup.find_all('img'):
        img_url = link.get('src')
        # отправляем запрос
        p = requests.get(img_url)
        img_name = formatter(img_url)
        # конвертируем все что есть в пнг
        # (свг не конвертируется) через Image
        if img_url[-3:] == 'svg':
            img_name = img_name[:50]
            svg2png(
                url=f'{img_url}', write_to=f'{save_folder}/{img_name}.png'
            )
        else:
            img_name = img_name[:50]
            im = Image.open(io.BytesIO(p.content))
            im.save(f'{save_folder}/{img_name}.png')
        # заменяем ссылки в файле на локальные
        link['src'] = f'{save_folder}/{img_name}.png'
        # запсываем соуп обратно в файл
        with open(f'{html_way}/{file_name}.html', 'w') as f:
            f.write(soup.prettify())

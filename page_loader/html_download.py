import os
import requests
from page_loader.img_download import img_downloader
from page_loader.support_func import formatter


# отталкиваемся везде от текущей директории
current_dir = os.getcwd()
# используем для скачивания хтмл


def download(url, save_dir=current_dir):
    result = requests.get(url)
    result = result.text
    file_name = formatter(url)
    full_file_name = file_name + '.html'
    save_url = save_dir + '/' + full_file_name
    f = open(f'{save_url}', 'w')
    f.write(f'{result}')
    f.close()
    img_downloader(save_dir, file_name, url)


#if __name__ == "__main__":
    #download()

download('https://ru.hexlet.io/courses')
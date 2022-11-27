import os
import requests


# отталкиваемся везде от текущей директории
current_dir = os.getcwd()
# используем для скачивания хтмл


def download(url, save_dir=current_dir):
    result = requests.get(url)
    result = result.text
    file_name = formatter(url)
    save_url = save_dir + '/' + file_name
    f = open(f'{save_url}', 'w')
    f.write(f'{result}')
    f.close()


def formatter(string):
    # обрезаем https/http
    replace_list = ['.', '/', '%', '_', ':']
    if string[:5] == 'https':
        string = string[8:]
    elif string[:5] == 'http:':
        string = string[7:]
    # заменяет лишние элементы в url и добавляет .html
    for elem in replace_list:
        string = string.replace(elem, '-')
    print(string + '.html')
    return (string + '.html')


if __name__ == "__main__":
    download()

import os
import urllib.request


# отталкиваемся везде от текущей директории
current_dir = os.getcwd()
# используем для скачивания хтмл
opener = urllib.request.FancyURLopener({})


def download(url, save_dir=current_dir):
    result = opener.open(url)
    result = result.read()
    file_name = formatter(url)
    save_url = save_dir + '/' + file_name
    print(save_url)
    f = open(f'{save_url}', 'w')
    f.write(f'{result}')
    f.close()
    print(f)


def formatter(string):
    # обрезаем https/http
    replace_list = ['.', '/', '%']
    if string[:5] == 'https':
        string = string[8:]
    elif string[:5] == 'http:':
        string = string[7:]
    # заменяет лишние элементы в url и добавляет .html
    for elem in replace_list:
        string = string.replace(elem, '-')
    return (string + '.html')


# url = '/home/ovechka/python-project-51/tests/fixtures/download.html'
if __name__ == "__main__":
    download()

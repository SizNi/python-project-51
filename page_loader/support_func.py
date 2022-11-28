def formatter(string):
    # обрезаем https/http
    replace_list = ['.', '/', '%', '_']
    if string[:5] == 'https':
        string = string[8:]
    elif string[:5] == 'http:':
        string = string[7:]
    # заменяет лишние элементы в url
    for elem in replace_list:
        string = string.replace(elem, '-')
    return string

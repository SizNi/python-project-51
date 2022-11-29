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

# проверяем совпадение домена,
# чтоб проверить, где хранятся метериалы
# если на том же домене - берем


def same_domain(string1, string2):
    string1 = formatter(string1)
    string2 = formatter(string2)
    ls1 = string1.split('-')
    ls2 = string2.split('-')
    if ls1[0] == ls2[0] and ls1[1] == ls2[1]:
        return True

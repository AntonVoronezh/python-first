def ret(st):
    if ' ' in st:
        return str(st).upper()
    else:
        return str(st).lower()


print(ret('giuy'))
print(ret('gi uy'))


def aaaa(a, b):  # позиционные аргументы
    return a + b


def aaaa2(f, a=0, b=0):  # именованные аргументы
    return a + b


def fff(*args):  # * - превращает в кортедж ()
    print(args)


fff(4, 5, 6)  # (4, 5, 6)


def ggg(**kwargs):  # ** - превращает в словарь {}
    print(kwargs)


ggg(ff=4, cc=5, dd=6)  # {'ff': 4, 'cc': 5, 'dd': 6}


def jjj(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


jjj(1, 2, 55, 66, f=0, y=8)

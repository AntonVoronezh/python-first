def aaaa(a, b):  # позиционные аргументы
    """
    Возвращает сумму аргументов а и б

    рангаешнагшн еншгашгнгш

    :param a: Парметр 1
    :type a: int

    :param b: Парметр 2
    :type b: int
    """
    return a + b


x = 5


def xx():
    global x  # внутри функции глобальные только для чтения, с помощтю global можно записывать
    x += 1


print(x)
xx()
print(x)

s = [1, 2, 3]


def get_ss():
    def aaaaa(x):
        return int(x) * 2

    return [aaaaa(i) for i in s]


print(get_ss())

s2 = [1, '2', 3]


def get_ss2(w):
    def aaaaa(x):
        if isinstance(x, int):
            return int(x) * 2

    return [aaaaa(i) for i in w if aaaaa(x)]


print(get_ss2(s2))


def get_ss3(w):
    def aaaaa(x):
        if isinstance(x, int):
            return x * 2

    return list(map(aaaaa, w))


print(get_ss3(s2))


def odd_ball(arr):
    index = arr.index('aaa')
    return index in arr


print(odd_ball(['jjj', 8, 'aaa', 1, 'bbb']))
print(odd_ball(['aaa', 0, 'bbb']))


def find_sum(a):
    dd = list(range(1, a + 1))
    ff = 0

    def yy(i):
        if i % 3 != 0 or i % 5 != 0:
            return i
        else:
            return 0

    ff += [yy(i) for i in dd]
    return ff


print(find_sum(5))

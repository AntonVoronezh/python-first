def ball(arr):
    return arr.index('odd') in arr


def sum(n):
    res = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res += 1
    return res


def sum2(n):
    return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)


g = ['aa', 'ffff', 'dd', 'yyy']


def hgg(k):
    return [i for i in k if len(i) == 2]


print(hgg(g))

t1 = (1, 2, 3)
print(type(t1))  # tuple

t2 = 1, 2, 3  # упаковка
print(type(t2))  # tuple

t3 = tuple((1, 2, 3))  # упаковка
print(type(t3))  # tuple

t = ()  # пустой
t4 = (1,)  # с одним элементом, нужна запятая - иначе будет int

f = tuple('dtyfttryt')
print(f)

y1 = (1, 2, 3,)
y2 = (12, 22, 32,)
print(y2 + y1)

print(len(f))

for i in f:
    print(i, end='  ')

t7 = ([111])
print(t7, id(t7))

t7[0] = 222
print(t7, id(t7))

hh = (1, 2, 3)
c, cc, ccc = hh
print(c, cc, ccc)

k = 1
k2 = 2

k, k2 = (k2, k)
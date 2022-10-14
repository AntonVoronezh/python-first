lis = [1, 2, 3, [22, 33], True, 'dty']

print(len(lis))
print(lis[3])
print(lis[:3])
print(lis[-2])

lis[0] = 'yjtfj'
print(lis)

lis[:2] = [111, 222]
print(lis)

lis.append(False)  # добавляет в конец
lis.extend([5, 6, 7])  # расширяет другим списокм - [111, 222, 3, [22, 33], True, 'dty', False, 5, 6, 7]
print(lis)

lll = ['@' * 2, 5]

lis += lll

print(lis)

lis.remove(5)  # удаляет первый найденный элемент

print(lis)

s = lis.pop()  # удаляет последний элемент или указанный индекс, возвращает его
s2 = lis.pop(5)  # удаляет последний элемент или указанный индекс, возвращает его

print(s, s2, end=' ')

fff = lis.copy()
print(fff)

# print(lis.sort()) # только однотипные значения
f = ['d', 'a', 'b']
f.sort()
print(f)

f2 = ['d', 'a', 'b']
f2.reverse()
print(f2)

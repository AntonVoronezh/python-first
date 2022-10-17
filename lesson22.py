s = {'aaaa', 'bbbb', 'ccccc', 'bbbb'}
s2 = set('hello')
s3 = {i for i in range(1, 11)}
s4 = set() # пустое множество, если сделать {} - то это будет словарь


print(type(s), s)
print(s2)
print(s3)

a = set('abracadabra')
b = set('alacazam')
c = a - b # убираем из а все буквы котрые есть в б
d = a | b # объединение - или в a или в b
e = a & b # пересечение - и в a и в b
f = a ^ b # множество из элементов - буквы в а или в б, но не в обоих

print(a, b, c, d, e, f, sep='\n')


ss = {'aaaa', 'bbbb', 'ccccc', 'bbbb'}
ss2 = s.copy() # делает копию
print(ss, id(ss))
print(ss2, id(ss2))

ss.add('ttt') # добавляет элемент

print(ss)

ss.remove('ttt') # удаляет элемент, если нет элемента - ошибка

print(ss)

ss.discard('ttt') # удаляет элемент, если нет элемента - НЕТ ошибки
print(ss)


ss.clear() # очистка

dd = frozenset('fjymjt') # замороженное множество





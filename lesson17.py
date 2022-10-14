x = 10
print(x, id(x))
x = 20
print(x, id(x))

x2 = 'aaa'
print(x2, id(x2))
x2 += '20'
print(x2, id(x2))

l = [1, 2, 3]
print(l, id(l))
l.append(0)
print(l, id(l))

q = 10
q2 = q

print(q, id(q))
print(q2, id(q2))

q = 15

print(q, id(q))
print(q2, id(q2))

l1 = [1,2,3]
l2 = l1

print(l1, id(l1))
print(l2, id(l2))

l1.append(5)
print(l1, id(l1))
print(l2, id(l2))

l2 = l1.copy() # l1[:]
print(l1, id(l1))
print(l2, id(l2))

sss = 10
print(sss)
del sss
print(sss)
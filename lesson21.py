words = ['мадам', 'топрот', 'madam', 'fjcyju']
words2 = []

for el in words:
    if el == el[::-1]:
        words2.append(el)


print(words2)

tt = [el for el in words if el == el[::-1]]
print(tt)

jj = ['Около Миши молоко', 'око За око']
kkk = []
for el in jj:
    el_r = el.replace(' ', '').lower()
    if el_r == el_r[::-1]:
        kkk.append(el)

print(kkk)

l = list(range(1,5))
l2 = tuple(range(1,5))
s = '-'.join(map(str, l))

print(s)




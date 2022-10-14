a = [1, 2, 3]
b = []

for i in a:
    b.append(i * 2)

print(a)
print(b)

# -----------------
c = 0
for i in b:
    c += i

print(c)

# -----------------

lit = 0.5
t1 = 3
t2 = 6.7
t3 = 11.8

print(int(t1 * lit))
print(int(t2 * lit))
print(int(t3 * lit))

# -----------------

ggg = 'hhhhh iiiii'

if ' ' in ggg:
    ggg = ggg.upper()
else:
    ggg = ggg.lower()

print(ggg)





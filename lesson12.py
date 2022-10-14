name = 'aaaa'
age = 20

x = 0

if x:
    print('111')
    print('#')
else:
    print('222')

light = 'red'

if light == 'red':
    print('stop')
elif light == 'yellow':
    print('rt')
else:
    print('go')

d = int(input('flglg '))

if d >= 18:
    print('ok')
else:
    print(f'no {18 - d}')


time = 10

if time > 5 or time < 3:
    print('11')
else:
    print('22')


day = 'st'
if time > 5 and day != 'ff':
    print('66')
else:
    print(88)

x = 1
if not x:
    print('1')
else:
    print(2)

# тернарник

f = 'sss' if x else 'bbb'
print(f)
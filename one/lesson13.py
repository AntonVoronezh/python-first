i = 1

while i <= 10:
    print(i, end=' ')
    i += 1


print('111', '222', sep='!', end='@')
print('111', '222', sep='#')

s = 'hello wo4rlfd'

for aaa in s:
    if aaa == '4':
        continue
    print(aaa, end=' ')


for i in 'ytitpuiyu tyu':
    if i == ' ':
        break
    print(f'#{i}# ', end=' ')
else: # это относится НЕ к if, а к for - раблтает в конце цикла, если вышли по break, то не работает
    print('\n no----')


start = 1900
end = 2022
t = start

while t <= end:
    print(t)
    t += 1
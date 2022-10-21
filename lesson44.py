import re

s = 'это просто строка текста ы7гве7г - это другая просто другая строка другая текста ы7гве7г'
pattern = 'строка'

print(s.find(pattern))
print(pattern in s)

if re.search(pattern, s):
    print('ok')
else:
    print('no')

mmm = re.search(pattern, s)
print(mmm)
print(mmm.end())
print(mmm.start())
print(mmm.span())

print(re.findall(pattern, s))
print(re.split(' ', s))



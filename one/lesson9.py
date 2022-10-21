a = r'sss \new' # r говорит что не нужно обрабатывать эту строку

a1 = 'qqqr'
a2 = 'ttt'
a3 = a1 + a2
dd = 6

print(a3 + str(dd))

print('hi' * 5)

print(a1[0])

print(a1[-1])

# a1[0] = '8' # TypeError: 'str' object does not support item assignment

fff = 'hello world'
# срезы [начало:конец:шаг]

print(fff[0:11]) # hello world
print(fff[:11]) # hello world

print(fff[6:]) #  world
print(fff[6:11]) #  world

print(fff[::2]) #  world

print(fff[::-1]) #  перевернуть - dlrow olleh

print(fff[:3] + fff[7:]) #  helorld



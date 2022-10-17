from random import randrange

rand_num = randrange(0, 10, 2)
print(fr'Введите число, {rand_num}')
user_num = int(input())

while user_num != rand_num:
    print(r'Неверно. попробуйте еще раз')
    user_num = int(input())

print('Ok! молодец')

def get_kv(num):
    return num ** 2


print(get_kv(5))

ggg = lambda num: num ** 2

print(ggg(10))

print((lambda num: num ** 2)(7))
print((lambda num, num2: num + num2)(7, 1))

li = [1, 2, 3]


# def get_double(l):
#     return [i * 2 for i in l]

def get_double(l):
    return list(map(lambda num: num * 2, l))

# print(get_double(li))

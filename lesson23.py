d = {}

prod_1 = {
    'title': 'sony',
    'price': 100
}
prod_2 = dict(title='iphobe', price=200)

print(prod_1)
print(prod_2)

user = [['aaa', 11], ['bbb', 222]]
d_user = dict(user)
print(d_user)

user2 = (('aaa2', 11), ('bbb2', 222))
d_user2 = dict(user2)
print(d_user2)

ff = dict.fromkeys(['aaa', 'gggg', 'hhhhh'], 100)
print(ff)

hh = {i: i+ 1 for i in range(1, 10)}
print(hh, type(hh[1]))

print(prod_1['title'])
print(prod_1.get('title'))

for key in prod_1:
    print(f'{key} & {prod_1[key]}')

for key, val in prod_1.items():
    print(key, val)

prod_3 = [
    {'title': 'sony', 'price': 100},
    {'title2': 'sony2', 'price2': 200},
]
prod_1 = {'title': 'hhh', 'price': 'uuuuuu'}

print(prod_1.items())
print(prod_1.keys())

# prod_1.pop('title', 'No') # удаляет ключ из словаря, второй параметр применяется если нет ключа

prod_1.setdefault('title22')
print(prod_1) # добавилось 'title22': None

prod_1.update({'yyy': 77}) # добавление в словарь, если есть то перезаписывает

print(prod_1.values())

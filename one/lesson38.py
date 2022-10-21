from one.classes import Person

a = Person('Fnd4ny5sr')

a.print_info()
# print(a._Person__age2)

# print(a.get_age())
a.set_age(100)
a.print_info()

print(f'decor - {a.age}')
a.age = 77
print(f'decor - {a.age}')

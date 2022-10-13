name = 'aaaa'
age = 20

print('my name ' + name + ' i am ' + str(age))

print('my name %(name)s i am %(age)d' % {'name': name, 'age': age})

print('my name %s i am %d' % ( name, age))

print('my name {} i am {}'.format(name, age))

print('my name {0} i {1} am {1}'.format(name, age))

print('my name {x} i am {y}'.format(x=name, y= age))

print(f'my name {name} i am {age + 7}')
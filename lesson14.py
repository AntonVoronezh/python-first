l1 = [1, 2, 3, [22, 33], True, 'dty']
l2 = list('rytrdty')
l3 = list((222, 3333))
l4 = [i for i in 'utffi yui']
l5 = [i for i in 'utffi yui' if i != ' ']
l5 = [i for i in 'utffi yui' if i not in ['f', 'i']]

print(l1, l2, l3, l4, l5, sep='\n')

l6 = list(range(5))  # [0, 1, 2, 3, 4]
l7 = list(range(3, 7))  # [3, 4, 5, 6]

print(l6, l7, sep='\n')

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}', end=', ')
    print(sep='')

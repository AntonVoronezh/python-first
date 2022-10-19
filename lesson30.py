# https://docs.python.org/3/library/

import os
import random as r
from random import randint, shuffle
# from random import *
import libs

print(os.getcwd())
print(r.randint(1, 100))
print(randint(1,40))

print(libs.get_count('fffff', 'g'))
print(libs.get_len('fffff'))

f = libs.get_count

print(f('fffff', 'g'))
try:
    # num = 100 / 0
    num = 100 / '0'
# except ZeroDivisionError:
#     num = 88
# except TypeError:
#     num = 44
except Exception: # любое исключение
    num = 677
else:
    print('else')
finally:
    print('finally')

print(num)


while True:
    try:
        num = int(input('dвведитеЖ '))
        print(f'100 / {num} = {100 / num}')
        break
    except ZeroDivisionError:
        print('---')
    except ValueError:
        print('+++')


# def hello():
#     return 'func "hello"'
#
#
# def super_func(func):
#     print('func "super_func"')
#     print(func())
#
#
# super_func(hello)
#
# def hello2():
#     return 'func "hello"'
#
# t = hello2
#
# super_func(t)

def my_decor(func):
    def func_wrapper():
        print('before')
        func()
        print('after')

    return func_wrapper


# @my_decor
# def func_test():
#     print('func "func_test"')
#
#
# # test = my_decor(func_test)
# # test()
#
# func_test()

def make_title(func):
    def func_wrapper():
        title = func()
        title = title.capitalize()
        return title

    return func_wrapper


@make_title
def hhh():
    return 'yutyuiftyuiyi'


print(hhh())

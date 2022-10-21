class Aaa:
    property1 = 'jjjj'  # свойство
    name = 'guest'

    def say_hi(self, name=''):
        if name:
            return 'hi ' + name
        else:
            return 'hi ' + self.name

a = Aaa()
b = Aaa()
# a.property1 = 'ddd'
print(a)
print(a.property1)
print(a.say_hi())

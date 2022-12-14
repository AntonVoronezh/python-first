class Person:
    def __init__(self, name):
        self.name = name
        self._age = 20  # private
        self.__age2 = 10  # private

    def print_info(self):
        print(f'Name: {self.name} + Age: {self._age} + Age2: {self.__age2}')

    def get_age(self):
        return self.__age2

    def set_age(self, age):
        if age in range(1, 101):
            self.__age2 = age
        else:
            self.__age2 = 99

    @property  # геттер декоратор
    def age(self):
        return self._age

    @age.setter  # сеттер декоратор
    def age(self, val):
        self._age = val


class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def print_info(self):
        super().print_info()
        print(f'11111111111111111111')

    def more_info(self):
        print(f'Name: {self.name} + Age: {self._age} + company: {self.company}')

    def __str__(self):
        # return f'name:::: {self.name}'
        return self.__class__.__name__

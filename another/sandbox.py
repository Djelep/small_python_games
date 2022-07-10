class Person:
    a = 15

    def __init__(self, name):
        self.__name__ = name

    @classmethod
    def print_info(cls):
        print(cls.a)

    @staticmethod
    def say_hello():
        print("hello")


Person.print_info()
Person.say_hello()

anton = Person("Anton")
anton.print_info()
anton.say_hello()
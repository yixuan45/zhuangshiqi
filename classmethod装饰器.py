class Person(object):
    @classmethod
    def say_hello(cls):
        print(f"我是{cls.__name__}")
        print("hello world!")


class Car(object):
    def say_hello(self):
        print(f"我是{self.__name__}")
        print("hello world!")


if __name__ == '__main__':
    Person.say_hello()
    car = Car()
    car.say_hello()

class Person:
    @staticmethod
    def say_hello():
        print("hello world!")


if __name__ == '__main__':
    per = Person()
    per.say_hello()
    Person.say_hello()

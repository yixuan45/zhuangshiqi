class User(object):
    def __init__(self, name, month_salary):
        self.name = name
        self.month_salary = month_salary

    @property
    def year_salary(self):
        return int(self.month_salary) * 12

    def print_hello(self):
        print('hello')
        return 10


if __name__ == '__main__':
    u1 = User("laoyang", "30000")
    print(u1.year_salary)
    print(u1.print_hello())

class MyLogDecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("日志记录。。。")
        return self.func(*args, **kwargs)


@MyLogDecorator
def func2():
    print("使用了功能2")


if __name__ == '__main__':
    func2()

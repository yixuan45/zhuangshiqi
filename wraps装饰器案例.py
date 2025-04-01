from functools import wraps


def mylog(func):
    @wraps(func)
    def infunc(*args, **kwargs):
        print("日志记录。。。")
        print("函数文档:", func.__doc__)
        return func(*args, **kwargs)

    return infunc


@mylog
def func2():
    """强大的功能2"""
    print("使用功能2")


if __name__ == '__main__':
    func2()
    print("函数文档---》", func2.__doc__)

# def outfunc(func):
#     def infunc():
#         print("使用记录log")
#         func()
#
#     return infunc
#
#
# def func1():
#     print("使用功能1")
#
#
# def func2():
#     print("使用功能2")
#
#
# func1 = outfunc(func1)
# func1()
# func2 = outfunc(func2)
# func2()


# def outfunc(func):
#     def infunc():
#         func()
#         print("日志记录")
#
#     return infunc
#
#
# @outfunc  # 相当于fun1=outfunc(fun1)
# def fun1():
#     print("使用功能1")
#
#
# @outfunc # 相当于fun2=outfunc(fun2)
# def fun2():
#     print("使用功能2")
#
#
# fun1()

# def mylog(func):
#     def infunc():
#         func()
#         print("日志记录")
#
#     return infunc
#
#
# @mylog  # 相当与func1=mylog(func1)
# def func1():
#     print("使用功能1")
#
#
# @mylog  # 相当与fuc2=mylog(func2)
# def func2():
#     print("使用功能2")
#
#
# func1()
# func2()

# def mylog(func):
#     def infunc(*args, **kwargs):
#         func(*args, **kwargs)
#         print("日志记录")
#
#     return infunc
#
#
# @mylog
# def func1():
#     print("使用功能1")
#
#
# @mylog
# def func2(a, b):
#     print(f"使用功能2:{a},{b}")
#
#
# func1()
# func2(100, 200)


# def example_function(*args):
#     for arg in args:
#         print(arg)
#
#
# example_function(1, 2, 3)  # 输出: 1, 2, 3

def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


example_function(a=1, b=2)  # 输出: a: 1, b: 2

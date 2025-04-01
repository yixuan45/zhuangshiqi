# class Demo(object):
#     def __call__(self, *args, **kwargs):
#         print('我是Demo')
#
#
# demo = Demo()
# demo()  # 直接调用对象，实质是调用了他的__call__()

class MyCallable:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value * x

    # 使用示例


obj = MyCallable(5)
result = obj(10)  # 这里调用了 obj 的 __call__ 方法
print(result)  # 输出 50

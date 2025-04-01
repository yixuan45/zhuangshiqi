import time


# 函数定义阶段：
# 相当于：
# func2=cost_time(func2)
# func2=mylog(func2)
# 也相当于:
# func2=mylog(cost_time(func2))
# 定义阶段:先执行cost_time函数,再执行mylog函数

def mylog(func):
    def infunc():
        print("添加记录！")
        func()

    return infunc


def cost_time(func):
    def infunc():
        now = time.time()
        time.sleep(2)
        func()
        print(f"花费的时间为{time.time() - now}秒")

    return infunc


@mylog
@cost_time
def func2():
    pass


# 调用执行阶段
# 先执行mylog的内部函数，再执行cost_time的内部函数

func2()

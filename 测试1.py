import time

j = 0
i = 1
a = 10000
x = 0
print("二的100000次方时间测试")
time_s = time.time()
for x in range(10):
    while j != a:
        i = i * 2
        j = j + 1
        y = x*10000+j
        print("第", y, "次，数值", i)
    j = 0
time_e = time.time()
TIME = time_e - time_s
print("本次计算用时", TIME, "秒")

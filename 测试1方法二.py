import time
i = 0
j = 100000
print("二的100000次方时间测试")
b = j + 1
time_s = time.time()
while i != b:
    a = 2**i
    print("第", i, "次，数值", a, "共", b, "次")
    i = i+1
time_e = time.time()
TIME = time_e - time_s
print("本次计算用时", TIME, "秒")

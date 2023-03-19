import time
print("π的4250位的计算")
time_s = time.time()
v = 4250
for n in range(0, v):
    t = n + 10
    b = 10 ** t
    x1 = b * 4 // 5
    x2 = b // -239
    s = x1 + x2
    n *= 2
    for i in range(3, n, 2):
        x1 //= -25
        x2 //= -57121
        x = (x1 + x2) // i
        s += x
    pai = s * 4
    pai //= 10 ** 10
    u = str(pai).split()
    u.insert(2, ".")
    pai1 = u
    print("第", n , "次，数值", pai1)
    n = n + 1
time_e = time.time()
TIME = time_e - time_s
print("共用时", TIME, "秒")
def func(num):
    def actual(x):
        return x**num
    return actual

var1 = func(2) #num
print(var1(3)) #x

var2 = func(3)
print(var2(3))
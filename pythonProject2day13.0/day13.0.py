def devide(a,b):
    if b == 0:
        raise IndexError("被除数不能为0")
    else:
        print(a/b)
try:
    devide(6,0)
except  Exception   as e:
    print("所有异常我都能解决",e)
except ZeroDivisionError    as  e:
    print("我处理了第一个异常",e)
    
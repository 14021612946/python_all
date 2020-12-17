'''
    python：
        56,23,25:整型（int）
        56.31:浮点数据(float,double)
        "hello world" "刘嘉伟"：字符串（str）
        True,False:布尔（boolean）
        元组：(1,4,5,6,6,8,2,10)  不可能在改变
        列表：[1,2,3,4,5,6,65,5,47] 数据可以随时改变
        字典：{
                "010":"南京"，
                "020":"上海"，

             }
             （键值对应关系。特点：不能存储重复数据。）
        集合：（1,5,7,8,9,9）：不能存储重复的数据
'''
'''
a = 56
b = "张家玮"
c = True
d = 6.32

print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''
'''
    列表：[]
    常用的api:
        len() 求长度


'''
'''print(a[0])
print(a[1])
print(a[2])
print("列表的长度：",len(a))
'''
'''
a = [-9, -5, -4, -2, -3, -7, -8, -9]

max = a[0]
index = -1
for i in range(0, len(a)):
    if a[i] >= max:
        max = a[i]
        index = i
print("a里的最大值为：", max, "，所对应角标为：", index)
'''
# 求所有数的和
# 方法1：
'''
a = [-9, -5, -4, -2, -3, -7, -8, -9]
num=0
for i in a:
    num=i+num
print(num)
'''
# 方法2：
'''
a = [-9, -5, -4, -2, -3, -7, -8, -9]
num=0
for i in range(0,len(a)):
    j=a[i]
    num=j+num
print(num)
'''
# 有以下一个列表，求其中是5的倍数的和
'''
a = [1,5,21,30,15,9,30,24]
num=0
for i in a:
    if i%5==0:
        num+=i
print('5的倍数的和为：',num)

'''
# 对第一题的列表进行排序
a = [1,5,21,30,15,9,30,24]
n=len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)









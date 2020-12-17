# # author:jason
# '''
# a = [2,5,4,3,6]
# sum = 0
#
# for i in a: # 不携带角标
#     sum += i # sum +=   i    a +=  n     a =  a + n
# print(sum)
# '''
# '''
#     列表：[]
#     常用的api:
#         len() 求长度
#         append() 可以向列表最后一位添加一条数据
#         remove（） 删除一个数
#         pop
#         切片：
#         枚举：列举出每一种可能出现的情况。enumerate()  index,value
#
#
# '''
# '''
# import  random
# names = ["刘日成","张佳伟","李晗聪","李晓帅","陆佳琪","刘营营","曹东雪","何登勇","张岩","洪晓雅"]
# # 切片：[start:end]  ,start  ~  end - 1
#
# print(names[0:3:2])
#
# names.append("贾生")
# names.remove("张佳伟")
# num =  int(random.random() * len(names))
# name = names[num]
# print("恭喜你，",name,"被点名！")
# print(names)
# '''
# # a = [1,2,3,4,5,6,7,8,9]
# # sum = 0
# # for i in a:
# #     sum = sum + i
# # print(sum)
# #
# # import random
# # names = ["刘莹莹","李晓帅","何登勇","曹东雪"]
# # num = int(random.random()*len(names))
# # name = names[num]
# # print(name)
# # import random
# # tree = [["小猪",20],["小母猪",30],["常青树",10],["柳树",40],["果树",60]]
# # tree.append("小狗")
# # tree.remove("果树")
# # tree.pop(小猪：常青树)
# # a = int(random.random()*len(tree))
# # b=tree[a]
# # print(b)
# # print(tree)
# # for index,value in enumerate(tree):
# #     print(index,"----",value)
# # print(tree[2][1])
# # print((tree[3][0]))
# #
# tree = [
#     ["小树",20],["大树",30],["常青树",10],["柳树",40],["果树",60]]
# mycart=[]
#
#
# while True:
#     for index, value in enumerate(tree):
#         print(index, " ", value)
#     choice = int(input("请输入您要买的商品"))
#     if choice.isdigit():
#         choice = int(choice)
#         if choice < len(tree):
#            if salary >= tree[choice][1]:
#               mycart.append(tree[choice])
#               salary = salary- tree[choice][1]
#               print("恭喜您，添加成功，您的余额剩余：",salary)
#            else:
#             print("对不起，您的余额不足，无法购买")
#         else:
#             print("您输入的数据有误，请重新输入：")
#     elif choice == 'q' or choice == 'Q':
#         print("欢迎下次光临")
#
#
#
# author:jason
shop = [
    ["Iphone",6000],
    ["Mac computer",12000],
    ["小米 watch",500],
    ["lenovo pc",4500],
    ["辣条",2.5],
    ["泡椒鸡爪",13],
    ["老干妈",10]
]
# 二维列表，一维列表又套个一维列表f
print("欢迎来到Jason超市购物广场".center(70,"-"))

# 1.先初始化自己的金钱
while True:
    salary = input("请输入您的初始金钱：")
    if salary.isdigit():# 判断输入的字符串是否能看成数字
        salary =  int(salary)
        print("恭喜您的您的初始金钱为",salary,"，祝您本次购物愉快！")
        break
    else:
        print("请重新输入您的初始余额！")

'''
    1. 输入商品编号
        1.1 输入不存在，打回去重新输入
        1.2 您的余额是否充足。买东西，需要将当前商品添加我的购物车里，余额还要减去那么多钱。
        1.3 若您的余额不足，强行退出。
    2.输入Q,q。退出商城。
    买的东西打一下小票。
'''
# 1.定义一个我的购物车
mycart = []

while True:
    # 展示所有商品
    for index, value in enumerate(shop):
        print(index, "  ", value)
    choice = input("请输入您要买的商品编号：")
    if choice.isdigit():
        choice = int(choice)
        if choice < len(shop):
            if salary >= shop[choice][1]:
                mycart.append(shop[choice]) # 添加到我的购物车
                salary -=  shop[choice][1]
                print("\033[32;20;1m恭喜你，添加成功！您的余额还剩：",salary,"\033[0m")
            else:
                print("\033[41;20;1m对不起，您的月不足，穷鬼！请退出!\033[0m")
        else:
            print("\033[42;20;1m您输入的商品编号它不存在！请重新输入\033[0m")
    elif choice  == 'q' or choice == 'Q':
        print("欢迎下次光临！！！")
        break
    else:
        print("\033[42;20;1m您的输入不合法，请重新输入！！！！\033[0m")
print("-------------------Bye!-------------------")


# 2.打印我的小票
for i in mycart:
    print(i)
print("您的余额为：",salary)
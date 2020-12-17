import  random
num = int(random.random() * 2000)
count = 0
while True:
    guess=int(input("请输入您要猜的数字："))
    count=count+1
    if num > guess:
        print("小了")
    elif num < guess:
            print("大了")
    else:
            print("恭喜您猜对了",num,"您猜的次数为",count,"次了")
            break








# class Human:
#     __name = None
#     __sex = None
#     __age = None
#     __remaining_money = None
#     __brand = None
#     __battery_capacity = None
#     __size = None
#     __duration = None
#     __integral = None
#
#     def __init__(self, name, sex, age, remaining_money, brand, battery_capacity, size, duration, integral):
#         self.__name = name
#         self.__sex = sex
#         self.__age = age
#         self.__remaining_money = remaining_money
#         self.__brand = brand
#         self.__battery_capacity = battery_capacity
#         self.__size = size
#         self.__duration = duration
#         self.__integral = integral
#
#     def setName(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     def setSex(self, sex):
#         self.__sex = sex
#
#     def getSex(self):
#         return self.__sex
#
#     def setAge(self, age):
#         self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#     def setRemaining_money(self, remaining_money):
#         self.__remaining_money = remaining_money
#
#     def getRemaining_money(self):
#         return self.__remaining_money
#
#     def setBrand(self, brand):
#         self.__name = brand
#
#     def getBrand(self):
#         return self.__brand
#
#     def setBattery_capacity(self, battery_capacity):
#         self.__battery_capacity = battery_capacity
#
#     def getBattery_capacity(self):
#         return self.__battery_capacity
#
#     def setSize(self, size):
#         self.__size = size
#
#     def getSize(self):
#         return self.__size
#
#     def setDuration(self, duration):
#         self.__duration = duration
#
#     def getDuration(self):
#         return self.__duration
#
#     def setIntegral(self, integral):
#         self.__integral = integral
#
#     def getIntegral(self):
#         return self.__integral
#
#     def messages(self):
#         print("我叫", .__name, y.__sex, y.__age, "岁了", "我的手机剩余话费有", y.__remaining_money,
#               "元！，手机品牌是", y.__brand, "电池容量是", y.__battery_capacity, "屏幕大小为", y.__size, "英寸",
#               "待机时长", y.__duration, "小时，剩余积分为", y.__integral)
#
#     def Phone(self):
#         h = input("请输入电话号码：")
class people:
    __username=None
    __sex=None
    __age=None
    __money=None
    __brand=None
    __ah=None
    __size=None
    __time=None
    __integrate=None

    def setUsername(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username
    def setSex(self,sex):
        self.__sex=sex
    def getSex(self):
        return self.__sex
    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age
    def setMoney(self,money):
        self.__money=money
    def getMoney(self):
        return self.__money
    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand
    def setAh(self,ah):
        self.__ah=ah
    def getAh(self):
        return self.__ah
    def setSize(self,size):
        self.__size=size
    def getSize(self):
        return self.__size
    def setTime(self,time):
        self.__time=time
    def getTime(self):
        return self.__time
    def setIntegrate(self,integrate):
        self.__integrate=integrate
    def getIntegrate(self):
        return self.__integrate
    def look(self):
        print(self.__username,self.__sex,self.__age,"您所拥有的手机剩余话费还有",self.__money,"您的手机品牌是",self.__brand,"您的电池容量是",self.__ah,"您的手机屏幕大小是",self.__size,"您的最大待机时长为",self.__time,"您所拥有的积分有",self.__integrate)
    def duanxin(self,msq):
         print(msq)
    def dadianhua(self):
         x=input("请输入您的手机号：")
         K=int(input("请输入你的通话时长："))
         if len(x) == None:
             print("您的电话号码不能为空：")
         elif p.__money < 1:
             print("您的余额不足，请充值")
         else:
             if 0 < K < 10 :
                 K=K*1
                 p.__money+=15
             elif 10 < K <20:
                 K=K*0.8
                 p.__money+=39
             else:
                 K=K*0.65
                 p.__money =p.__money+48
             print("请输入您要拨打的电话号码")



p=people()
p.setUsername("小明")
p.setSex("男")
p.setAge(18)
p.setMoney(10)
p.setBrand("华为")
p.setAh(3600)
p.setSize("17寸")
p.setTime("7.04小时")
p.setIntegrate(2033)
p.look()
p.duanxin("刘莹莹是猪")
p.dadianhua()

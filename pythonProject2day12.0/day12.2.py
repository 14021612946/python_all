# class jisuanqi:
#     __jia=None
#     __jian=None
#     __cheng=None
#     __chu=None
#
#     def __init__(self,jia,jian,cheng,chu):
#         self.__jia=jia
#         self.__jian=jian
#         self.__cheng=cheng
#         self.__chu=chu
#
#     def setJia(self,jia):
#         self.jia=jia
#     def getJia(self):
#         return self.__jia
#     def setJian(self,jian):
#         self.jia=jian
#     def getJian(self):
#         return self.__jian
#     def setCheng(self,cheng):
#         self.cheng=cheng
#     def getCheng(self):
#         return self.__cheng
#     def setChu(self,chu):
#         self.chu=chu
#     def getChu(self):
#         return self.__chu
class Calculator:

    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        print(sum)
        # sum = self.__num + self.__num1
        # print(self.__num,"+",self.__num1,"=",sum)

    def subtract(self,*args):
        sub=args[0]
        for i in args[1:]:
            sub-=i
        print(sub)


    def multiply(self,*args):
        mul=1
        for i in args:
            mul*=i
        print(mul)


    def divide(self,*args):
        div=args[0]
        for i in args[1:]:
            div/=i
        print(div)
        # div = self.__num / self.__num1
        # print(self.__num,"÷",self.__num1,"=",div)

c=Calculator()
c.add(2,3)
c.subtract(20,1)
c.multiply(2,3)
c.divide(3,5)
class Air:
    __prand=None
    __price=None

    def setPrand(self,prand):
        self.__prand=prand
    def getPrand(self):
        return self.__prand
    def setPrice(self,price):
        self.__price=price
    def getPrice(self):
        return self.__price
    def open(self,time):
        print("空调将会在",time,"分钟后自动关闭")
    def temp(self,temp):
        print("您的温度是:",temp,"度")
        print(self.__prand,"空调开机了","价格是",self.__price)


p=Air()
p.setPrand("美的")
p.setPrice("588")
p.open(90)
p.temp(22)







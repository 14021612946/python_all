class Dog:
    __color=None
    __speed=None
    def  __init__(self,c,d):
        self.__color = c
        self.__speed = d

    def setColor(self,c):
        self.__color=c
    def getColor(self):
        return self.__color
    def setSpeed(self,d):
        self.__speed=d
    def getSpeed(self):
        return self.__speed
d = Dog("红色","犬科")

print(d.getColor(),"科目",d.getSpeed(),)




class student:
    __username=None
    __age=None
    __deskmatename=None
    __daskmateage=None
    def setUsername(self,username):
        self.__username=username
    def getUsername(self):
        return self.__username
    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age
    def setDaskmatename(self,daskmatename):
        self.__daskmatename=daskmatename
    def getDaskmatename(self):
        return self.__daskmatename
    def setDaskmateage(self,daskmateage):
        self.__daskmateage=daskmateage
    def getDaskmateage(self):
        return self.__daskmateage
    def daskmate(self):
        print("大家好","我叫",self.__daskmatename,"我今年",self.__daskmateage,"岁了")
    def presentation(self):
        print("大家好","我叫",self.__username,"我今年",self.__age,"岁了！")
    #
    # def compare(self):
    #     if self.__age>self.__daskmateage:
    #         print("我比同桌大",(self.__age-self.__daskmateage),"岁")
    #     elif self.__age<self.__daskmateage:
    #          print("我比同桌大",(self.__age-self.__daskmateage),"岁")
    #     else:
    #           print("我和同桌一样大")
    def Compare(self,p1):
        if self.__age > p1.getAge():
            print("我比同桌大",self.__age - p1.getAge(),"岁")
        elif self.__age<p1.getAge():
            print("我比同桌小",p1.getAge() - self.__age,"岁")
        else:
            print("我和同桌一样大")






p=student()
p.setUsername("小明")
p.setAge(15)
p.presentation()

p1=student()
p1.setUsername("小花")
p1.setAge(27)



p.Compare(p1)




class people:
    __name = None
    __age = None

    def __set_name__(self,name,age):
        self.__name = name
        self.__age = age

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
    def show(self):
        print("大家好，我叫",self.__name,"我的年龄是:",self.__age)

    def bijiao(self,p1):
        if self.__name = p1.getName()


p=people()
p.setName("小花")
p.setAge(12)
p.show()


p1=people()
p1.setName("小明")
p1.setAge(24)



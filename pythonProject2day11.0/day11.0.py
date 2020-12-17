class Person:
    __username = ""
    __age =None
    def setUsername(self,u):
        self.__username=u

    def setAge(self,a):
        if a == None:
            print("年龄非法")
        elif a>120 or a<0:
            print("年龄非法")
        else:
            self.__age = a
    def show(self):
        print("我叫",self.__username,"我的年龄",self.__age)

p= Person()

p.setUsername("何登勇")
p.setAge=(22)
p.show()






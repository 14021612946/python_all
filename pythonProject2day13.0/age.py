from you import YouException
class person:
    __age=None

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def compare(self):
        if self.__age   >  0:
            print("您的年龄是",self.__age)
        else:
            raise YouException("输入非法")


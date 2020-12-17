from aaa import AaaaException
class jianshe:
    __yue = 3000



    def getYue(self):
        return self.__yue


    def compare(self,p):
        if p < self.getYue():
            print("余额充足")
        else:
            raise AaaaException("金额不足异常")



k=jianshe()
a = int(input('请输入'))
k.compare(a)

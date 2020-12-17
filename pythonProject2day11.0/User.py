import datetime
from tools import tools
class User:
     __account =None  #系统自动产生，不需要提过set方法，可以提过get方法
     __username=None
     __password=None
     __address=None
     __money=None
     __reg_date=None#不需要提供set方法，可以提过get方法
     __bankname=None#不需要提供set方法，可以提供get方法

     def __init__(self,username,password,address,money):
        self.__username=username
        self.__password=password
        self.__address=address
        self.__money=money
        self.__account=tools().getRandom()
        self.__bankname="中国工商银行昌平支行"
        self.__reg_date=datetime.datetime

     def getAccount(self):
         return self.__account
     def getBankname(self):
         return self.__bankname
     def getReg_date(self):
         return self.__reg_date
     def setUsername(self,username):
         self.__suername=username
     def getUsername(self):
         return self.__username
     def setPassword(self,password):
         self.__password=password
     def getPassword(self):
         return self.__password
     def setAddress(self,address):
         self.__address=address
     def getDaress(self):
         return self.__address
     def setmoney(self,money):
         self.__money=money
     def getmomey(self):
         return self.__money
c=User("账号","注册时间","开户行","姓名")
print("账号：",c.getAccount(),"注册时间：",c.getReg_date(),"开户行：",c.getBankname(),"姓名：",c.getUsername(),"密码：",c.getPassword(),"地址",c.getDaress(),"余额",c.getmomey())


















name=input("请输入姓名")
idnumber=input("请输入身份证号")
age=int(input("请输入年龄"))
gender=input("请输入性别")
hight=input("请输入身高")
weight=input("请输入体重")

#  姓名  年龄  性别  身份证号  身高   体重
info='''
-----------------中国公民身份信息--------------
姓名:{name}
年龄：{age}
性别：{gender}
身份证号：{idnumber}
身高：{hight}
体重:{weight}
--------------------------------------------
'''
print(info.format(name=name,age=age,gender=gender,idnumber=idnumber,hight=hight,weight=weight))


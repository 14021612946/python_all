f = open("a.txt","w+",encoding="utf-8")
f.write("姓名:密码:年龄:性别\n")
f.write("jason:admin:56:男\n")
f.write("张三:root:35:女\n")
f.write("王五:1qaz2wsx:rootadmin:男\n")
f.write("赵六:12afqe:weer:女\n")
f.close()
a = {}
f =open("a.txt","r+",encoding="utf-8")
date = f.readlines()
for i in date:
    line = i . split(":")
    a[line[0]]=line[1].replace("\n","")
name=input("请输入您的名字")
password=input("请输入您的密码")
age=input("请输入您的年龄")
sex=input("请输入您的性别")
if name in a :
   if password == a[name]:
      print("登陆成功")
   else:
       print("密码输入错误")
else:
    print("该用户名不存在")

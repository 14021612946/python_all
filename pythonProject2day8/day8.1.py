# f = open("123.jpg","rb")
# w = open("图片.jpg","wb")
# date = f.read()
# w.write(date)
# f.close()
# w.close()
a={}
f = open ("c.txt", "r+", encoding="utf-8")
date=f.readlines()
for i in date :
    line = i . split(":")
    a[line[0]]=line[1].replace("\n","")
name = input("请输入您的用户名:")
password = input("请输入您的密码:")
if name in a:
   if password == a[name]:
       print("登陆成功")
   else:
       print("密码输入错误")
else:
    print("该用户名不存在")
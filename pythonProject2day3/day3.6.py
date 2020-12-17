a = int(input("请输入长度："))
b = int(input("请输入长度："))
c = int(input("请输入长度："))
if a > 0 and b > 0 and c > 0 and  a + b > c and b + c > a and a + c > b :
    if ( a * a + b * b == c * c ) or ( a * a + c * c == b * b ) or ( c * c + b * b == a * a ):
        print("直角三角形")
    elif ( a * a + b * b < c * c ) or (a * a + c * c < b * b) or ( c * c + b * b < a * a ) :
        print("普通三角形")
    elif ( a * a == b * b == c * c ) :
        print("等边三角形")
else:
   print("输入错误")







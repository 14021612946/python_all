# import  xlrd
# date = xlrd.open_workbook('E:\\my\\yhgl.xlsx')
# sheet = date.sheet_by_name("用户管理")
# print(("有",sheet.nrows,"行数据！","有",sheet.ncols,"列数据"))
# rows = sheet.nrows
# cols = sheet.ncols
# f = open("用户管理.txt","w",encoding="utf-8")
# a=[]
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         a.append(str(sheet.cell_value(i,j)).replace(".0",""))
#     string = ",".join(a)
#     f.write(string+"\n")
#


class girl:
    high = 0 #她的身高
    hair = "" #她的头发
    leg = ""  #她的腿
    look="" #她的长相

    def go(self):
        print("当秋叶落下，地上满是金黄，她走过来，周遭的环境仿佛为之一动，片片落叶煽动，欢迎这远方而来的佳人")

her = girl()
her. high =1.7
her.hair = "black"
her.leg = "纤细笔直"
her.look= "一脸俏容"
her.go()
print(("那个佳人她身高",her.high,"米","头发颜色",her.hair,"她的腿",her.leg,"她的面庞",her.look))


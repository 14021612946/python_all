class oldphone:
    phonenumber=None
    voice=None

    def call(self,number):
     print(self.phonenumber,"正在给",number,"打电话。。。。")
class Newphone(oldphone):
    place = None
    picture = None
    ps = None

    def call(self,number):
        super().call(number)
        print("归属地：",self.place,"图片",self.picture,"备注",self.ps)

phone = Newphone()
phone.phonenumber="12345324354"
phone.voice="月亮之上"
phone.place = "河北"
phone.picture = "野猪佩奇"
phone.ps = "旺财来电"
phone.call("143654366")

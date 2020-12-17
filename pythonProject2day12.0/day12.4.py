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
    print("")



import unittest
import yinhang

class TestBank(unittest.TestCase):

    def testSaveUser(self):
        account = 123456
        password = 123
        country = 456
        province = 788
        street = 990
        door = "贵州"
        money = 1000
        exept = True
        haha = yinhang.bank_addUser(account,password,country,province,street,door,money)
        print(haha)

        self.assertEqual(exept,haha)

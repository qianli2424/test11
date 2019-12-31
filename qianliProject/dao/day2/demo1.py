# -*- coding=utf8 -*-
#@author:qianli
# 文件说明：假设有一个商城，用vip用户。用户有用户名name，有账户余额money。我们在创建对象（办卡）的时候
#就会要求我们输入用户名和余额。还有系统的名称system_name=fsmarket

class vip:
    def __init__(self,name,money=0):
        self.name = name
        self._money = money
    def show(self):
        print('您的fsmarket系统的用户名为：{0}，当前余额为：{1}'.format(self.name,self._money))
    def addmoney(self,money=100):
        #省略代码若干
        self._money += money
    def shopping(self,money):
        self._money -= money
'''
有一个svip账户，有三个属性：name，money，score（积分），账户名和金额是一样的
关于充值addmoney方法，和vip类是一样的做法
关于消费shopping方法，不仅金额减少，还会产生相应的积分
它还多一个积分对象exchange(score)方法，每100个积分兑换成1元
'''
class svip(vip):
    def __init__(self,name,money=0,score=0):
        super().__init__(name,money)        #通过引用方法来搬代码，这个叫做继承
        self._score=score
    def show(self):     #因为父类方法能力不足，所以需要重写以加强
        super().show()  #仍然可以先引用父类的方法进行处理  父类名.show(self)
        print('您的积分为：{}'.format(self._score))
    def shopping(self,money):
        super().shopping(money)
        self._score += money
if __name__=='__main__':
    s = svip('admin',100,50)
    s.addmoney(25)
    s.show()
    s.shopping(98)
    s.show()
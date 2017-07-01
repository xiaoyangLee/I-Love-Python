# -*- coding=utf-8 -*-
'''
演示List的引用
'''
class Klass: 
    l = [ 1,2,3,4 ]
    def __init__(self,name=''):
        self.name=name

k1=Klass()
k2=Klass()
k3=Klass()

k1.l[1] = 0
print (k1.l,k2.l,k3.l)

k2.l = 0
print(k1.l,k2.l,k3.l)

Klass.l = 0
print(k1.l,k2.l,k3.l)

'''
解释和说明：

根据Python自己的属性搜索优先级，k1.l[1] = 0会优先寻找类Klass中的属性，即k1,k2,k3三个对象引用的list.

所以k1.l ,k2.l ,k3.l的值都会被改变。

但是如果k2.l = 0这种情况下，Python会优先给k2.l引用一个新的属性l，并赋值0.
故不会影响到k1.l 和 k3.l的值.

'''

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



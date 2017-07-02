# -*- coding=utf-8 -*-
'''
将help()帮助信息输出到一个help.txt文档中。
这里使用了sys.stdout
输出重定向。
'''
import sys
import os

out = sys.stdout
sys.stdout = open("help.txt","w")
help(str)
sys.stdout.close()
sys.stdout = out
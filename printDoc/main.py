#-*- coding= utf-8 -*-
"该文件主要用作打印stand.py中的文档和变量信息"
import stand;
import time;

print stand.__doc__

print stand.new_str

print stand.hello()

#time.time()获取unix时间戳,从1970年开始。
print time.time()

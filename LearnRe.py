#-*- coding:utf-8 -*-
"文档说明:学习Python的正则表达式,替换要处理的文本"
import re
keyword = "南京  市长 江大桥   欢迎您"
#keyword = "南京市长江大桥"
#找到所有的空格,都替换为/
keyword = re.sub(r' ', '/',keyword)

print keyword
#keyword = "南京//市长/江大桥///欢迎您"

#正则说明:/*/,表示查找字符串中至少含有一个/或者多个/的字符,并都替换为一个','
pattern = '/*/'
keyword = re.sub(pattern, ',', keyword)

print keyword

#split分词,将关键字提取到列表中
list_keyword = keyword.split(',')

#使用迭代打印出列表中的中文信息,如果直接打印会是Unicode编码
for x in list_keyword:
    print x

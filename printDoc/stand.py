#coding= utf-8

#这种其实可以任意写。但是需要符合#coding[:=]\s*([-\w.]+)

"这是一个标准模块脚本的写作范式，此处为该脚本文档。"

#这里给下面的脚本添加一个注释
new_str="定了一个全局变量"  #这里定义了一个全局变量，为字符串类型

def hello():
	"""
	这里是一个函数的多行注释
	我可以连着写几行说明
	@author
	@copyright
	"""
	return "hello world"


#程序主体语句
if __name__=="__main__":
	print hello()

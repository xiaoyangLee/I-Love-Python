#!/usr/bin/env python
# coding:utf-8
import base64
import hashlib

'''
NCTF Program编程题 根据加密写解密
Author@Xiaoyang
说明:加密是进行了位运算和base64编码
核心思想是,对一个数值进行异或后,得到的结果再次进行异或会得到原文。
'''

def encrypto(string):
    str1 = ""
    for i in string:
        str1 += chr((ord(i) + 8) ^ 0x16)
    str2 = ""
    for j in base64.b64encode(str1):
        str2 += chr(ord(j) ^ 0x32)
    str3 = ""
    for k in base64.b64encode(str2):
        str3 += chr(ord(k) ^ 0x64)
    return base64.b64encode(str3)

#根据encrypto()加密函数写成的解密函数
def decrypty(string):
    str3 = ""
    #先将已经被base64编码的结果用base64译码
    string = base64.b64decode(string)
    for k in string:
        #依次将每个字符的ASCII数值进行异或运算,还原成被第二步base64编码的原文
        str3 += chr(ord(k) ^ 0x64)
    #把原文进行base64译码
    str3 = base64.b64decode(str3)

    str2 = ""
    for j in str3:
        #依次将每个字符的ASCII数值进行异或运算,还原成被第一步base64编码的原文
        str2 += chr(ord(j) ^ 0x32)
    #把原文进行base64译码
    str2 = base64.b64decode(str2)

    str1 = ""
    for i in str2:
        #对加密的第一步进行逆推,先将上面得到的结果进行异或,随后再-8得到正确的字符。
        str1 += chr((ord(i) ^ 0x16)-8)
        
    return str1

def flag(string):
    flag = "python_is_the_best" + string
    return str(hashlib.md5(flag.encode('utf-8')).hexdigest())

def main():
    #将网页上显示加密过后的结果输入进来
    ciper = "MlUXIzw8UQwnExRRPAkMCAE8NjMnClEGJlYyTwEPMiUCCiIjJjI2UjcDMlEHMT4VAgoUJz48USgzNVxZ"
    print "nctf{" + flag(decrypty(ciper)) + "}"

if __name__ == "__main__":
    main()
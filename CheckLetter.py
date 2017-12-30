# -*- coding: utf-8 -*-
# @Time    : 2017/9/2 16:02
# @Author  : libin.zhao
# @Email   : 783044971@qq.com
# @File    : test.py
# @Software: PyCharm
def normalize(name):
    if name == None and name == '':return None
    namelist = list(name)
    if ord(namelist[0]) in range(97,122):
        namelist[0] = chr(ord(namelist[0]) - 32)
    for index,ch in enumerate(namelist[1:]):
        if ord(ch) in range(65,91):
            namelist[1+index] = chr(ord(namelist[1+index]) + 32)
        else:
            continue
    return ''.join(namelist)




def getClimbCount(n,result):
    if n ==0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return  2
    if n in result:
       return result[n]
    else:
        value = getClimbCount(n-1,result) + getClimbCount(n-2,result)
        result[n] = value
        return value
def getClimbCount_1(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1



#-*- coding: UTF-8 -*-

'''
    1、读取指定目录下的所有文件
    2、读取指定文件，输出文件内容
    3、创建一个文件并保存到指定目录
    '''
import os
import string
import random

filesPath = []

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        #print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
        if os.path.isdir(child):
            eachFile(child)
        else:
            if ".h" in child or ".m" in child:
                filesPath.append(child)
    return filesPath

def addCode(arr):
    for filename in arr:
        fopen = open(filename, 'r') # r 代表read
        lines = fopen.readlines()
        fopen.close

        fopen = open(filename, 'w') # r 代表read
        for k,v in enumerate(lines):
            if '\\' in v:
                fopen.write(v)
            else:
                str = autoStr('//') + '\n'
                fopen.write(v+str)
        fopen.close()

def autoStr(str):
    wList = []
    for word in string.lowercase:
        wList.append(word)
    num = random.randint(10, 20)
    list = random.sample(wList,num)
    randomstr = ''.join(list)
    return str + randomstr

if __name__ == '__main__':
    filePath = "."
    fileArr = eachFile(filePath)
    print fileArr
    addCode(fileArr)




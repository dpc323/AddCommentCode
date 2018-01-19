#-*- coding: UTF-8 -*-

import os
import string
import random

filesPath = []

# 遍历指定目录下的所有文件名以及子文件夹内文件名
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

#自动添加注释
def addCode(arr):
    for filename in arr:
        fopen = open(filename, 'r') # r 代表read
        lines = fopen.readlines()
        fopen.close

        fopen = open(filename, 'w') # w 代表write
        for k,v in enumerate(lines):
            if '\\' in v:       #用'\'分行写的代码，如果此时添加注释会引起报错
                fopen.write(v)
            else:
                str = autoStr('//') + '\n'
                fopen.write(v+str)
        fopen.close()

#生成10-20个数字的随机注释代码
def autoStr(str):
    wList = []
    for word in string.lowercase:
        wList.append(word)
    num = random.randint(10, 20)
    list = random.sample(wList,num)
    randomstr = ''.join(list)
    return str + randomstr

if __name__ == '__main__':
    filePath = "."    #从当前python文件所在文件目录遍历文件，包含当前文件夹
    fileArr = eachFile(filePath)
    print fileArr
    addCode(fileArr)




# -*- coding: utf-8 -*-

###################################################
# 处理tag末尾含逗号的信息
#
###################################################
import re
import time

s = time.time()
f = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\results\fileItem.txt','r')

pattern = re.compile(r".*,$")

result = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\results\fileReplace.txt', 'a')
sum = 0

for item in f.readlines():
    itemList = item.strip().split('\t')
    tag = itemList[1]
    mat = re.match(pattern,tag)
    sum = sum + 1
    if(mat is not None):
        newTag = tag[:len(tag)-1]
        newItem = itemList[0] + '\t' + newTag + '\t' + itemList[2] + '\n'
        print newItem
        result.write(newItem)
        
    else:
        result.write(item)

print sum  # 1703436
print "duration time: " + str(time.time() - s)

result.close()
f.close()
# -*- coding: utf-8 -*-

####################################
# 根据tag_all中的tag_sorted（过滤后的标签集合）过滤原tas文件中的信息
# 将标签集合未出现的tag所在的信息过滤掉
# 未处理tag末尾含逗号的标签，在tag_replace中进行处理
#
###################################
from tag_all import tag_sorted
import time
#import re
tasFile = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\tas','r')

#读取每一行信息，将tag转化为小写，并与过滤之后tag集合进行匹配
resultFile = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\results\fileItem.txt', 'a')

sum = 0

s = time.time()
# tag_sorted中未将末尾含逗号的tag替换掉
for item in tasFile.readlines():
    itemList = item.strip().split('\t')
    tag = itemList[1].lower()
    for i in range(len(tag_sorted)):
        if(tag == tag_sorted[i]):
            # 保留 user / tag / content_id 三部分信息
            newItem = itemList[0] + '\t' + tag + '\t' + itemList[2] + '\n'
            print newItem
            resultFile.write(newItem)
            sum = sum + 1
        else:
            continue
            
        
print "duration time:" + str(time.time()-s)
print sum    #1676187

resultFile.close()
tasFile.close()
 
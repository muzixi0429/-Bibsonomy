# -*- coding: utf-8 -*-
##########################################
# 对已经过滤的fileItem 进行处理
# 收集同一个resource 对应的tag集合
# fileItem中的信息： user / tag / content_id
###########################################、
f1 = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\results\fileReplace.txt', 'r')

res_tag_Dic = {}
listTag = []
for item in f1.readlines():
    itemList = item.strip().split('\t')
    resource = itemList[2]
    tag = itemList[1]
    listTag.append(tag)
    #将当前tag追加到key对应的value中，value值是字符串，用/t间隔
    if(res_tag_Dic.has_key(resource)):
        newValue = res_tag_Dic[resource] + "/t"  + tag
        res_tag_Dic[resource] = newValue
    #新建key-value对
    else:
        res_tag_Dic[resource] = tag

print "----------------------------------------------"
print "resource num： " + str(len(res_tag_Dic))
print "tag num:  " + str(len(list(set(listTag))))
print "----------------------------------------------"
f1.close()


#res_tag_Dic
# 将value值转化为list
for key in res_tag_Dic.keys():
    valueList = res_tag_Dic[key].strip().split('/t')
    res_tag_Dic[key] = valueList
print len(res_tag_Dic)

####------------------------------------------------
## 统计词对共现
# 1. 词对
# 2. 统计词对共现的次数


lenList = len(listTag)
tagPairList = []
for i in range(lenList):
    for j in range(lenList):
        pair = (listTag[i], listTag[j])
    tagPairList.append(pair)

print len(tagPairList)


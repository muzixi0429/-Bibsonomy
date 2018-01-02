# -*- coding: utf-8 -*-

###########################################
# filter tag
# 1. 从tas中将tag抽取出来
# 2. 统计词频
# 3. 将词长小于2 ,大于20，且词频低于50 的tag过滤掉
# 4. tag转化为小写
# 5. 过滤tag
#   --> 过滤 含有 *，{}，[],纯数字，_开头的，末尾含数字的
#   --> 过滤 非英文tag
#   --> tag末尾的,进行替换
#
###########################################
import re

#将tas文件中的tag标签全抽取出来，包含重复的tag
tas = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\tas','r')
tag = [line.strip().split('\t')[1] for line in tas.readlines()]
tas.close()
print "num of all tags: " + str(len(tag))

#对tag进行的词频进行统计
tagDic = {}
for i in range(len(tag)):
    if(tagDic.has_key(tag[i])):
        tagDic[tag[i]] = tagDic[tag[i]] + 1
    else:
        tagDic[tag[i]] = 1
print "num of tags(no repeat):" + str(len(tagDic))

#对字典中的value进行排序
tagDic_sorted = sorted(tagDic.items(),key = lambda item: item[1])


# 将排序后的字典写入文件中
'''
f = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\sortDic.txt','a')
for i in range(len(tagDic_sorted)):
    f.write(tagDic_sorted[i][0] + '\t' + ":" + '\t' + str(tagDic_sorted[i][1]) + '\n') 
f.close()
'''

#将词长小于2 ,大于20，且词频低于50 的词过滤掉
tagList = []
for i in range(len(tagDic_sorted)):
    if(len(tagDic_sorted[i][0]) > 2 and len(tagDic_sorted[i][0]) < 20 and tagDic_sorted[i][1] > 50):
        tagList.append(tagDic_sorted[i][0])
    else:
        continue
print "num of tags of first filter: " + str(len(tagList))   #


#所有tag转化为小写
tagList01 = [item.lower() for item in tagList]

##——------------------------------------------------------------

#使用正则表达式过滤tag
# 含有 *，{}，[],纯数字，_开头的，末尾含数字的
p = r"(.*(\*|\+|{|\[|\<|:|\\|/|;).*)|(^\d{1,5})|(.*\d{2,5}$)|(^_)"
pattern = re.compile(p)
tagList02 = []
for i in range(len(tagList01)):
    mat = re.match(pattern,tagList01[i])
    if mat is not None:  
        #print tagList01[i]
        continue
    else:
        tagList02.append(tagList01[i])
print "num of tags of second filter: " + str(len(tagList02))


# 过滤非英文tag
pattern = re.compile(r".*[\x90-\xff]+.*")
tagList03 = []
for i in range(len(tagList02)):
    mat = re.match(pattern, tagList02[i])
    if mat is not None:
        #print tagList03[i]
        continue
    else:
        tagList03.append(tagList02[i])
print "num of tags of third filter: " + str(len(tagList03))


#将个别tag末尾的逗号remove(指示替换，因此tag数并没有变化)
pattern = re.compile(r".*,$")
tagList04 = []
for i in range(len(tagList03)):
    mat = re.match(pattern,tagList03[i])
    if mat is not None:
        #print tag[i]
        #print tag[i][:len(tag[i])-1]
        tagList04.append(tagList03[i][:len(tagList03[i])-1])
    else:
        tagList04.append(tagList03[i])
print "num of tags of fourth filter: " + str(len(tagList04))


###过滤完成----------------------------------------------------------------
#过滤完成的tagList04去重
tag = list(set(tagList04))
print "total tag: " + str(len(tag))

#对最终的tag进行排序
tag_sorted = sorted(tag)


"""
#将过滤完成并排序的tag写入文件中
tag_file = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\results\tag_filter.txt','a')
for i in range(len(tag_sorted)):
    tag_file.write(tag_sorted[i]+"\n")
"""  



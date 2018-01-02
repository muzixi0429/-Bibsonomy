# -*- coding: utf-8 -*-

################################################
# 将从wordnet中抽取出来的上位词，下位词，同义词与tag中进行匹配，抽取pair
#################################################

import tag_all,tagInWordNet

#tag = tag_all.tag_sorted  #处理完成的之后的标签
#numTag = len(tag)

#从tag list中查找是否存在给定的word
def findWord(word):
    tag = tag_all.tag_sorted
    for i in range(len(tag)):
        if(tag[i] == word):
            return True
        else:
            continue
    return False

#遍历同义词字典，以list的形式返回
#list中的元素是tuple，tuple中的元素是具有同义词关系的两个word

synDic = tagInWordNet.syn_Dic
hyponDic = tagInWordNet.hypon_Dic
hyperDic = tagInWordNet.hyper_Dic

#同义词
synList = []
for key in synDic.keys():
    #遍历key对应的value的list中的每一个word，检索其是否存在于tag list中
    # 如果存在则与可以组成tuple，追加list synList之后。
    lenValue = len(synDic[key])
    for i in range(lenValue):
        if(findWord(synDic[key][i])):  #检索到，返回True
            tup =(key,synDic[key][i])
            synList.append(tup)
        else: #未检索到，返回False
            continue
print "len of syn: " + str(len(synList))

#上位词
hyperList = []
for key in hyperDic.keys():
    lenValue = len(hyperDic[key])
    for i in range(lenValue):
        if(findWord(hyperDic[key][i])):
            tup = (key,hyperDic[key][i])
            hyperList.append(tup)
        else:
            continue
print "len of hyper: " + str(len(hyperList))
         
#下位词
hyponList = []
for key in hyponDic.keys():
    lenValue = len(hyponDic[key])
    for i in range(lenValue):
        if(findWord(hyponDic[key][i])):
            tup = (key,hyponDic[key][i])
            hyponList.append(tup)
        else:
            continue
print "len of hypon: " + str(len(hyponList))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
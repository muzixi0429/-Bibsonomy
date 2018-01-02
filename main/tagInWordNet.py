# -*- coding: utf-8 -*-

##############################################
# 从wordnet中获取每个tag的同义词，上位词，下位词
#
##############################################
import tag_all
from nltk.corpus import wordnet

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#同义词

        
def word_syn(word):
    synonyms = []
    for syn in wordnet.synsets(word): #同义词集
        for lemma in syn.lemmas():  #同义词集下的词条
            synonyms.append(lemma.name())
    synonyms = list(set(synonyms))
    return synonyms

#下位词
def word_hyper(word):
    hypernym = []
    for syn in wordnet.synsets(word): #词的同义词集
        for hyper in syn.hypernyms(): # 同义词集中每个词的下位词集合
            for lemma in hyper.lemmas(): # 每个下位词集的lemma
                hypernym.append(lemma.name())
    hypernym = list(set(hypernym))
    return hypernym
 

#上位词   
def word_hypon(word):
    hyponyms = []
    for syn in wordnet.synsets(word): #词的同义词集
        for hypon in syn.hyponyms(): # 同义词集中每个词的下位词集合
            for lemma in hypon.lemmas(): # 每个下位词集的lemma
                hyponyms.append(lemma.name())
    hyponyms = list(set(hyponyms))
    return hyponyms
  
# --------------------------------------------
  

tag = tag_all.tag_sorted  #处理完成的之后的标签
numTag = len(tag)
#print len(tag)
    
# 收集同义词
syn_Dic = {} # tag - value
for i in range(numTag):
    value = word_syn(tag[i])
    syn_Dic[tag[i]] = value
        
numSyn = 0 
synFile = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\results\syn.txt','a')
for key in syn_Dic.keys():
    if(len(syn_Dic[key]) != 0):
        numSyn  = numSyn + 1
        synFile.write(key + "\t" + ":" + str(syn_Dic[key]) + "\n" )
    else:
        continue
synFile.close()
print "numSyn:" + str(numSyn)
    
# 收集上位词
hyper_Dic = {}
for i in range(numTag):
    value = word_hyper(tag[i])
    hyper_Dic[tag[i]] = value
    
numHyper = 0 
hyperFile = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\results\hyper.txt','a')
for key in hyper_Dic.keys():
    if(len(hyper_Dic[key]) != 0):
        numHyper  = numHyper + 1
        hyperFile.write(key + "\t" + ":" + str(hyper_Dic[key]) + "\n" )
    else:
        continue
hyperFile.close()
print "numHyper:" + str(numHyper)
        
# 收集下位词
hypon_Dic = {}
for i in range(numTag):
    value = word_hypon(tag[i])
    hypon_Dic[tag[i]] = value
        
numHypon = 0 
hyponFile = open(r'C:\Users\mengyi\Desktop\exp\bibsonomy\results\hypon.txt','a')
for key in hypon_Dic.keys():
    if(len(hypon_Dic[key]) != 0):
        numHypon  = numHypon + 1
        hyponFile.write(key + "\t" + ":" + str(hypon_Dic[key]) + "\n" )
    else:
        continue
hyponFile.close()
print "numHypon:" + str(numHypon)
    
        
    
    
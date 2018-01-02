# -*- coding: utf-8 -*-

from  resource_tag_collection import lr
from tag_all import tag

lenlr = len(lr)
print lenlr

lentag = len(tag)
print lentag
flag = False

for i in range(lenlr):
    for j in range(lentag):
        if(lr[i] == tag[i]):
            flag = True
            break
        else:
            continue
    # tag中没有和lr[i]相同的
    if(flag == False):
        print "------------"
        print lr[i]
        print "------------"
    
    else:
        flag = False
        
        



#!/usr/bin/python
# -+- coding: utf-8 -+-
import re,os
import pickle
import sys,math
from numpy import *
import matplotlib.pyplot as plt
from decimal import *
contain_dict_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "contain.pkl")
fin=open(contain_dict_path, 'rb')
contain = pickle.load(fin) #将contain字典取出来
fin.close()
numOfKeywords=int(len(contain)*0.2)
print "There are %d keywords selected!!!"%numOfKeywords

d=sorted(contain.iteritems(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
selected_keywords_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "selected_keywords.txt")
selected_keywords_fout=open(selected_keywords_path,'w')
for k in range(numOfKeywords):
  selected_keywords_fout.write(d[k][0].encode('utf-8')+'\n')
selected_keywords_fout.close()

selected_keywords=[d[k][0] for k in range(numOfKeywords)]
print len(selected_keywords)

type_keyword_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "type_keyword.pkl")
fin=open(type_keyword_path, 'rb')
type_keyword = pickle.load(fin) #将contain字典取出来
fin.close()

stat_dict=dict()
for keyword in selected_keywords:
  for keyword_type in type_keyword:
    if keyword in type_keyword[keyword_type]:
      t=keyword_type; break #找到词语的类型
  stat_dict[t]=stat_dict.get(t,0)+1
print stat_dict
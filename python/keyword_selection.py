#!/usr/bin/python
# -+- coding: utf-8 -+-
import re,os,sys
import string
reload(sys)
sys.setdefaultencoding('utf-8')
split_100000_dis_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "split_100000_dis.txt")
fin=open(split_100000_dis_path)
keyword_dict=dict()
for line in fin:
  line=unicode(line.strip(), "utf-8")
  keyword_list=line.split(unicode('|','utf-8'))
  for keyword in keyword_list:
    keyword_dict[keyword]=keyword_dict.get(keyword,0)+1
fin.close()

d=sorted(keyword_dict.iteritems(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
selected_keywords_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "selected_keywords.txt")
fout=open(selected_keywords_path,'w')
number=0
for keyword,weight in d:
  number+=1
  if number>4000: #选择的keyword数量
    break
  else:
    fout.write(keyword.encode('utf-8')+'\n')

fout.close()
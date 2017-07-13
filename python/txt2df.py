#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os,sys
from pandas import Series,DataFrame
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')
starttime = datetime.datetime.now()    
######################################################    
selected_keywords_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "selected_keywords.txt")
selected_keywords=[]
with open(selected_keywords_path, "r") as fin:
  for line in fin.readlines():
    line=unicode(line.strip(), "utf-8")
    selected_keywords.append(line)

type_industry_labels_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "sample_60000.txt")
fin=open(type_industry_labels_path)
all_lines=fin.readlines()
row_num=len(all_lines)
print "There are %d lines in the input file!!!"%row_num
# default_columns=[u'男性',u'女性'] #
default_columns=selected_keywords
col_num=len(default_columns)
df=DataFrame(np.zeros((row_num,col_num)),columns=default_columns)

for row,line in enumerate(all_lines): #row：0,1,2,3,...
  # print "line %d is processing, %s has beed used. Please wait ..." % (row+1,(datetime.datetime.now() - starttime))
  line=unicode(line.strip(),'utf-8')
  # label,keywords=line.split(unicode(',','utf-8'),1)
  # df.ix[row,u'类别']=label
  keywords_list=line.split(unicode('|','utf-8'))
  for element in keywords_list:
    if element in selected_keywords:
      df.ix[row,element]=1 #自动添加列

df.fillna(0,inplace=True) #默认不为NAN,而是为0

columns_path=os.path.join(os.path.split(os.path.realpath(__file__))[0], "all_columns.txt")
columns_fout=open(columns_path,'w')
for column_name in df.columns: #将列名写到文件
    columns_fout.write(column_name+'\n')
columns_fout.close()

matrix_file_path=type_industry_labels_path=os.path.join(os.path.split(os.path.realpath(__file__))[0], "matrix_file.csv")
df.to_csv(matrix_file_path,index=False) #将表格写到文件
fin.close()
# print df.columns
print df.shape #输出表格的行列数

#####################################################
endtime = datetime.datetime.now()
print (endtime - starttime),"time used!!!" #0:00:00.280797
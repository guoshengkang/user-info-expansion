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
sample_60000_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "sample_60000.txt")
fout=open(sample_60000_path,'w')

split_60000_dis_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "split_60000_dis.txt")
fin=open(split_60000_dis_path)
all_lines=fin.readlines()
row_num=len(all_lines)
selected_line_nos=np.random.permutation(range(row_num))
selected_line_nos_60000=selected_line_nos[:30000]
print len(selected_line_nos_60000)
for row,line in enumerate(all_lines): #row：0,1,2,3,...
  if row in selected_line_nos_60000:
    line=unicode(line.strip(),'utf-8')
    fout.write(line.encode('utf-8')+'\n')
fin.close()

split_100000_dis_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "split_100000_dis.txt")
fin=open(split_100000_dis_path)
all_lines=fin.readlines()
row_num=len(all_lines)
selected_line_nos=np.random.permutation(range(row_num))
selected_line_nos_100000=selected_line_nos[:30000]
print len(selected_line_nos_100000)
for row,line in enumerate(all_lines): #row：0,1,2,3,...
  if row in selected_line_nos_60000:
    line=unicode(line.strip(),'utf-8')
    fout.write(line.encode('utf-8')+'\n')
fin.close()
fout.close()
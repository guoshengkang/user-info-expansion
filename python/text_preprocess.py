#!/usr/bin/python
# -+- coding: utf-8 -+-
import re,os
import pickle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import datetime
starttime = datetime.datetime.now()

def split_dict(dict_str):
  keywords=[]
  dict_str=dict_str.strip('{}')
  dict_list=dict_str.split(unicode(';','utf-8'))
  for d in dict_list:
    keyword,value=d.split(unicode(':','utf-8'))
    if keyword.isdigit():
      pass #去掉数字关键词
    else:
      keywords.append(keyword)
  return keywords

def split_array(array_str):
  array_str=array_str.strip('[]')
  keywords=array_str.split(unicode(';','utf-8'))
  return keywords

input_file_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "160000_life.csv")
output_16_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "split_160000.txt")
output_6_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "split_60000.txt")
output_10_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "split_100000.txt")
dictionary_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "dictionary.txt")

fout16=open(output_16_path,'w')
fout6=open(output_6_path,'w')
fout10=open(output_10_path,'w')

dictionary=set() #所有的词汇
dictionary60000=0
dictionary100000=0

type_keyword={'tag_psb':[],'token_t':[],'subroots':[],'gender':[],'occupation':[],'level_edu':[]}

line_no=0
with open(input_file_path, "r") as fin:
  for line in fin.readlines():
    # try:
    line_no+=1
    keywords=[]
    line=unicode(line.strip(), "utf-8")
    (mobile_no,label,tag_psb,token_t,subroots,gender,occupation,level_edu)= line.split(unicode(',','utf-8'))
    #mobile_no,label,tag_psb,token_t,subroots,gender,occupation,level_edu
    
    # tag_psb 
    # if tag_psb!=u'NULL':
    #   tag_psb=split_dict(tag_psb)
    # else:
    #   tag_psb=[]
    # keywords.extend(tag_psb)
    # type_keyword['tag_psb'].extend(tag_psb) #扩充
    # type_keyword['tag_psb']=list(set(type_keyword['tag_psb'])) #去重

    # token_t 去掉物品描述的关键词
    if token_t!=u'NULL':
      token_t=split_dict(token_t)
    else:
      token_t=[]
    keywords.extend(token_t)
    type_keyword['token_t'].extend(token_t) #扩充
    type_keyword['token_t']=list(set(type_keyword['token_t'])) #去重

    #subroots 去掉物品类别的关键词
    # if subroots!=u'NULL':
    #   subroots=split_array(subroots)
    # else:
    #   subroots=[]
    # keywords.extend(subroots)
    # type_keyword['subroots'].extend(subroots) #扩充
    # type_keyword['subroots']=list(set(type_keyword['subroots'])) #去重

    if gender!=u'NULL':
      keywords.append(gender)
      type_keyword['gender'].append(gender) #扩充
      type_keyword['gender']=list(set(type_keyword['gender'])) #去重
    if occupation!=u'NULL':
      keywords.append(occupation)
      type_keyword['occupation'].append(occupation) #扩充
      type_keyword['occupation']=list(set(type_keyword['occupation'])) #去重
    if level_edu!=u'NULL':
      keywords.append(level_edu)
      type_keyword['level_edu'].append(level_edu) #扩充
      type_keyword['level_edu']=list(set(type_keyword['level_edu'])) #去重

    dictionary=dictionary|set(keywords)
    new_line='|'.join(list(set(keywords))).encode('utf-8')
    fout16.write(label.encode('utf-8')+','+new_line+'\n')
    if label==u'60000':
      fout6.write(new_line+'\n')
      dictionary60000=dictionary60000+len(keywords)
    if label==u'100000':
      fout10.write(new_line+'\n')
      dictionary100000=dictionary100000+len(keywords)
    # except Exception as e:
    #   print "There may be something wrong in line:%s"%line_no
    #   print 'string: [%s] message:[%s]' % (line, e)
    #   continue

fout16.close()
fout6.close()
fout10.close()

print "There are %d keywords in dictionary60000 !!!"%dictionary60000
print "There are %d keywords in dictionary100000 !!!"%dictionary100000

type_keyword_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "type_keyword.pkl")
output_type_keyword=open(type_keyword_path, 'wb')
pickle.dump(type_keyword, output_type_keyword) #save pickle可以存取任意类型的数据
output_type_keyword.close()

dict_fout=open(dictionary_path,'w')
for keyword in dictionary:
  dict_fout.write(keyword.encode('utf-8')+'\n')
dict_fout.close()

print "There are %d keywords in dictionary!!!"%len(dictionary)

endtime = datetime.datetime.now()
print "There are %s time used!!!"%(endtime - starttime) #0:00:00.280797
print "Finished!!!!"
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve,auc
from sklearn.cross_validation import train_test_split
import numpy as np
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

# arr=np.loadtxt('U_60000xk.txt',delimiter=',')
arr=np.load('U_60000xk.npy') 
y=[1]*30000; y.extend([0]*30000)
X_train,X_test,y_train,y_test=train_test_split(arr,y,test_size=0.2,random_state=0)
print len(y_train),X_train.shape
print len(y_test),X_test.shape
# indexes=range(25000); indexes.extend(range(30000,55000))
# y=[1]*25000; y.extend([0]*25000)
# X=arr[indexes,:]
# print len(y),X.shape
# y_test=[1]*5000; y_test.extend([0]*5000)
# indexes_test=range(25000,30000); indexes_test.extend(range(55000,60000))
# X_test=arr[indexes_test,:]
# y_test=y
# X_test=X
# print len(y_test),X_test.shape

lr=LogisticRegression(C=1000.0,random_state=0)
lr.fit(X_train,y_train)
# print lr.coef_ #输出矩阵:class_num*dimension (6L, 369L)
# print lr.intercept_ #输出截距 class_num个元素
coefficients=lr.coef_
intercepts=lr.intercept_

probas=lr.predict_proba(X_test) #计算测试样本的得分
fpr, tpr, thresholds = roc_curve(y_test, probas[:,1], pos_label=1)

index1=[];index0=[]
for index,x in enumerate(y_test):
  if x==1:
    index1.append(index)
  else:
    index0.append(index)

score1=probas[index1,1]
print 'before:',score1.shape
score1=(0.135927*score1)/(1-0.864073*score1)
print 'after:',score1.shape

score0=probas[index0,1]
print 'before:',score0.shape
score0=(0.135927*score0)/(1-0.864073*score0)
print 'after:',score0.shape
# score1=probas[0:25000,1]
# score0=probas[30000:55000,1]

score_stat_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "score_stat.csv")
fout=open(score_stat_path,'w')
interval=0.05
N1=[];N0=[]
for start in arange(0,1.0,interval):
  end=start+interval
  num1=0
  for x in score1:
    if start<=x<end:
      num1+=1
  num0=0
  for x in score0:
    if start<=x<end:
      num0+=1
  N1.append(num1);N0.append(num0);
  line="[%.2f-%.2f),%d,%d"%(start,end,num1,num0)
  fout.write(line+'\n')
fout.close()

print(auc(fpr, tpr))

fig=plt.figure()
plt.plot(range(len(N1)),N1,label='positive')
plt.plot(range(len(N0)),N0,label='negative')
plt.legend(loc='best')
plt.show() 

# fig=plt.figure()
# plt.plot(fpr,tpr,label='ROC')
# plt.plot([0,1],[0,1],linestyle='--',label='random guessing')
# plt.legend(loc='best')
# plt.show() 
# error_stat=0.0 #统计预测结果,错误率
# for k in range(25000,30000):
#   x=arr[k,:]
#   result=lr.predict(x)
#   print result,type(result)
#   if result==array([0]): #预测错误
#     error_stat+=1
# print "error_num=%f error_rate=%f"%(error_stat,error_stat/5000)

# k=1089
# Sigma=np.load('Sigma.npy') 
# print Sigma.shape
# Sigk=mat(eye(k)*Sigma[:k])
# VT_nxn=np.load('VT.npy')
# V_nxk=VT_nxn[:k,:].T #np.shape(V_nxk)
# weight_life_service=V_nxk*Sigk.I*coefficients.T #n*6
# intercepts_life_service=intercepts
# np.savetxt('weight_life_service.txt',weight_life_service,fmt='%.9f',delimiter=',')
# np.savetxt('intercepts_life_service.txt',intercepts_life_service,fmt='%.9f',delimiter=',')

#!/usr/bin/user_gender
#-*-coding:utf-8-*-
import numpy as np
import pandas as pd
import pprint
import pickle
from sklearn import preprocessing
import datetime

def find_k_dim(arr):
    arr = arr ** 2
    total = sum(arr)
    arr = arr.cumsum()
    threshold = 0.8 * total
    for index, item in enumerate(arr):
        if item >= threshold:
            return index+1

starttime = datetime.datetime.now()
print 'reading file ...'
arr=np.loadtxt('svd_samples_60000.txt',delimiter=',',skiprows=1)
print "%s time has beed used for reading file ..." % (datetime.datetime.now() - starttime)
print arr.shape

print "-- start SVD --"
starttime = datetime.datetime.now()
U,Sigma,VT=np.linalg.svd(arr)
print "-- end SVD --: %s time has beed used..." % (datetime.datetime.now() - starttime)

k=find_k_dim(Sigma)
print 'there are %d columns after reducing dimensions!!!' % k

U_mxk=U[:,:k]
np.savetxt('U_mxk.txt',U_mxk,delimiter=',')

print "start saving results of SVD"
starttime = datetime.datetime.now()
np.savetxt('U.txt',U,delimiter=',')
np.savetxt('Sigma.txt',Sigma,delimiter=',')
np.savetxt('VT.txt',VT,delimiter=',')
np.save('U.npy',U)
np.save('Sigma.npy',Sigma)
np.save('VT.npy',VT)
print "end saving results of SVD: %s time has beed used ..." % (datetime.datetime.now() - starttime)

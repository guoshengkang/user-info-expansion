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
Sigma=np.load('Sigma.npy') 
k=find_k_dim(Sigma)
print 'there are %d columns after reducing dimensions!!!' % k
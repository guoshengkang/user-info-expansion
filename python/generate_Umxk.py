#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
from numpy import *
import datetime

starttime = datetime.datetime.now()
print 'reading file ...'
U_mxn=np.loadtxt('svd_samples_60000.txt',delimiter=',',skiprows=1)
print "%s time has beed used for reading file ..." % (datetime.datetime.now() - starttime)
print U_mxn.shape

k=583
Sigma=np.load('Sigma.npy') 
print Sigma.shape
Sigk=mat(eye(k)*Sigma[:k])
VT_nxn=np.load('VT.npy')
V_nxk=VT_nxn[:k,:].T #np.shape(V_nxk)
U_60000xk=mat(U_mxn)*V_nxk*Sigk.I
print U_60000xk.shape

starttime = datetime.datetime.now()
print "saving U_60000xk.txt..."
np.savetxt('U_60000xk.txt',U_60000xk,delimiter=',')
print "saving U_60000xk.npy..."
np.save('U_60000xk.npy',U_60000xk)
print "end saving files: %s time has beed used ..." % (datetime.datetime.now() - starttime)
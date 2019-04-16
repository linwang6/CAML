#' Please cite our paper if our paper or code helped you.
#' 


###################################

import re
import os
import sys
import imp
import warnings
#warnings.filterwarnings('ignore')
import numpy as np
#from matplotlib import pyplot
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from imblearn.ensemble import RUSBoostClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import classification_report
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import train_test_split
from pycm import *

###################################

outputType=open(sys.argv[1],'r')#'%s'%sys.argv[10]
outpurSubType=open(sys.argv[2],'r')#'%s'%sys.argv[10]+'subType'
outpurMergType=open(sys.argv[3],'w')



outputTypeL={}
for line in outputType:
    line=line.strip()
    lineE=line.split()
    if int(len(lineE))>1:
      if '"' in lineE[0]:
        outputTypeL[lineE[0]]=lineE[-1]

outputTypeSub={}
for line in outpurSubType:
    line=line.strip()
    lineE=line.split()
    if int(len(lineE))>1:
      if '"' in lineE[0]:
        if lineE[0] in outputTypeL.keys():
            outputTypeL[lineE[0]]=lineE[-1]


#typeP=[]
#for cellID in TypePreL.keys():
 #   typeP.append(outputTypeL[cellID])



#confusionMatrix = confusion_matrix(cellTypesTrue, cellTypesPred)
#cm = ConfusionMatrix(actual_vector=typeT, predict_vector=typeP)
#print >>outpurMergType,'Post-Classification Model Evaluation'
#print >>outpurMergType,cm

for line in outputTypeL.keys():
    print >>outpurMergType,line,outputTypeL[line]
    

outputType.close()
outpurSubType.close()
outpurMergType.close()



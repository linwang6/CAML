#'
#'
#'
#'
#'
#' 
#' Requiements:
#' 1. Istall R, version 3.4 or greater
#' 2. Python 2.7 or greater
#' 3. Packages:
#'    'Open R'
#'    install.packages("Seurat")
#'    library(Seurat)
#'    'Python'
#'    numpy (>=1.8.2)
#'    scipy (>=0.13.3)
#'    scikit-learn (>=0.20)
#'    imbalanced-learn (0.4)
#'    pip install -U numpy
#'    pip install -U scipy
#'    pip install -U scikit-learn
#'    pip install -U imbalanced-learn
#'    pip install -U sklearn
#' Please cite our paper if our paper or code helped you.
#' 
#' @example
#' python2.7, /usr/local/bin/python2.7 caml_test.py
#' python 3.6,  python caml_test.py 

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

##### Check inputs #####

##### checking training file #####

###################################

trainFile=open(sys.argv[1],'r')#The traning file

exLtrain=[]
exMtrain=[]
cellTypesTrain=[]


for line in trainFile:
    line=line.strip()
    lineE=line.split()
    if 'ypes' not in line:
         for j in range(1,int(len(lineE))-1):
             exLtrain.append(float(lineE[j]))
         cellTypesTrain.append(lineE[int(len(lineE))-1])
         exMtrain.append(exLtrain)
         #s.append("\n")
         exLtrain=[]
         

cellTypesTrain = np.array(cellTypesTrain)
exMtrain = np.array(exMtrain)


##### checking prediction file #####


exLpred=[]
exMpred=[]
cellID=[]
cellTypesTrue=[]
###################################

predFile=open(sys.argv[2],'r')#The prediction file

for line in predFile:
    line=line.strip()
    lineE=line.split()
    if '"' not in lineE[1]:
         for j in range(1,int(len(lineE))):
             exLpred.append(float(lineE[j]))
         #cellTypesTrue.append(lineE[int(len(lineE))-1])
         exMpred.append(exLpred)
         #s.append("\n")
         exLpred=[]
         cellID.append(lineE[0])


#cellTypesTrue = np.array(cellTypesTrue)
exMpred = np.array(exMpred)
cellID = np.array(cellID)

###################################

##### Everything is ready for cell type prediction #####

rusboost = RUSBoostClassifier(random_state=0)
rusboost.fit(exMtrain, cellTypesTrain)

##### Cell types prediction #####
cellTypesPred = rusboost.predict(exMpred)

#accuracy_score = balanced_accuracy_score(cellTypesTrue, cellTypesPred)
#print accuracy_score
#classification_report(cellTypesTrue, cellTypesPred)

##### Checking performance #####
#confusionMatrix = confusion_matrix(cellTypesTrue, cellTypesPred)
cellTypesProbs = rusboost.predict_proba(exMpred)
#print confusionMatrix
##### Merging the cell types and probability score #####

cellID_Probs = np.concatenate((cellID[:,None],cellTypesProbs),axis=1)
combine = np.concatenate((cellID_Probs,cellTypesPred[:,None]),axis=1)

###################################

##### Output the results from array #####
# file format:
# Cell_ID Cell_types_prediction Cell_types_prediction_probability_score
#
##### Prediction complete, and generate the output file #####

outFile=open(sys.argv[3],'w')#The name of output file

element=''

#cm = ConfusionMatrix(actual_vector=cellTypesTrue, predict_vector=cellTypesPred)
#print "\n"
#print "Post-Classification Model Evaluation:\n"
#print cm

#print >>outFile,'Post-Classification Model Evaluation'
#print >>outFile,cm

for line in combine:
    #line=line.strip()
    #lineE=line.split()
    for j in range(0,int(len(line))):
        element=element+line[j]+'       '
    print >>outFile,element
    element=''

#cm = ConfusionMatrix(actual_vector=cellTypesTrue, predict_vector=cellTypesPred)
#print cm
    
##### Done #####


trainFile.close()
predFile.close()
outFile.close()

###################################

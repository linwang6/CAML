#' ELSA: Cell type Auto classification of scRNA-Seq or snRNA-Seq via Machine Learning
#' 
#' Single-cell RNA sequencing (scRNA-seq), a powerful research tool, enables rapid determination of 
#' the precise gene expression patterns of tens of thousands of individual cells and has broad 
#' applications across biomedical research. Cell type annotation of scRNA-Seq data is the first and 
#' one of the most important step for downstream analysis and affects data interpretation, which is  
#' challenging due to: a. imbalanced scRNA-seq data (small cell popultation of data set, i.e. 
#' there is less than 1% T cell in brain tumor), b. lower number of detected genes of snRNA-Seq 
#' (compatibility with frozen samples), which is also labor intensive and tends to generate biased annotation.
#' Overall, there is lack of one high accurency auto annotation tool for scRNA-Seq or snRNA-Seq in the single cell sequencing era.
#' Here, we present one novel high accurency auto annotation method (ELSA) for scRNA-Seq or snRNA-Seq, especially for 
#' the imbalanced single cell data. ELSA integrates the RUSBoost algorithm, which can alleviate the problem of 
#' class imbalance by combining data sampling and boosting, improving classification performance when training data is imbalanced.
#'
#'
#'
#'
#'
#' 
#!/usr/bin/python
#' Requiements:
#' 
#' 1. Python 2.7 or greater
#' 2. Packages:
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
#'
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

if len(sys.argv) < 11:
    print """

Usage: elsa_v1.py [-t] [-p] [-c] [-g] [-o] [-s]

arguments:
  -t, --traning           traning prep data
  -p, --prediction        prediction prep data
  -c, --cell_type         cell type list
  -g, --geneNum           number of top importances
  -o, --output            output file for cell types
  -s, --specify           specific cell type for extending

"""

###################################
if len(sys.argv) == 11:
	addType='/usr/local/bin/python2.7 ../resources/addType.py '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[2]+' '+'%s'%sys.argv[2]+'_addType'
	os.system(addType)
	featureSelection='/usr/local/bin/python2.7 ../resources/feature_selection_RF.py '+'%s'%sys.argv[2]+'_addType'+' '+'%s'%sys.argv[2]+'_featureImportance'
	os.system(featureSelection)
	featureSort='sort -k 2 -r -g '+'%s'%sys.argv[2]+'_featureImportance >'+'%s'%sys.argv[2]+'_featureImportanceSort'
	os.system(featureSort)
	featureTop='head -n '+'%s'%sys.argv[8]+' '+'%s'%sys.argv[2]+'_featureImportanceSort >'+'%s'%sys.argv[2]+'_featureImportanceTop'+'%s'%sys.argv[8]
	os.system(featureTop)
	train='/usr/local/bin/python2.7 ../resources/parse_getID4matrixEx.py '+'%s'%sys.argv[2]+'_featureImportanceTop'+'%s'%sys.argv[8]+' '+'%s'%sys.argv[2]+' '+'%s'%sys.argv[2]+'_featureImportanceTopTrain'
	os.system(train)
	pred='/usr/local/bin/python2.7 ../resources/parse_getID4matrixEx.py '+'%s'%sys.argv[2]+'_featureImportanceTop'+'%s'%sys.argv[8]+' '+'%s'%sys.argv[4]+' '+'%s'%sys.argv[4]+'_featureImportanceTopPred'
	os.system(pred)
	trainType='/usr/local/bin/python2.7 ../resources/addType.py '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[2]+'_featureImportanceTopTrain'+' '+'%s'%sys.argv[2]+'_featureImportanceTopTrainType'
	os.system(trainType)
	#predType='/usr/local/bin/python2.7 ../resources/addType.py '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[4]+'_featureImportanceTopPred'+' '+'%s'%sys.argv[4]+'_featureImportanceTopPredType'
	#os.system(predType)
	elsa='/usr/local/bin/python2.7 ../resources/run_elsa.py -t '+'%s'%sys.argv[2]+'_featureImportanceTopTrainType'+' -p '+'%s'%sys.argv[4]+'_featureImportanceTopPred'+' -o '+'%s'%sys.argv[10]
	os.system(elsa)


###################################
if len(sys.argv) == 13:
	addType='/usr/local/bin/python2.7 ../resources/addType.py '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[2]+' '+'%s'%sys.argv[2]+'_addType'
        os.system(addType)
        featureSelection='/usr/local/bin/python2.7 ../resources/feature_selection_RF.py '+'%s'%sys.argv[2]+'_addType'+' '+'%s'%sys.argv[2]+'_featureImportance'
        os.system(featureSelection)
        featureSort='sort -k 2 -r -g '+'%s'%sys.argv[2]+'_featureImportance >'+'%s'%sys.argv[2]+'_featureImportanceSort'
        os.system(featureSort)
        featureTop='head -n '+'%s'%sys.argv[8]+' '+'%s'%sys.argv[2]+'_featureImportanceSort >'+'%s'%sys.argv[2]+'_featureImportanceTop'+'%s'%sys.argv[8]
        os.system(featureTop)
        train='/usr/local/bin/python2.7 ../resources/parse_getID4matrixEx.py '+'%s'%sys.argv[2]+'_featureImportanceTop'+'%s'%sys.argv[8]+' '+'%s'%sys.argv[2]+' '+'%s'%sys.argv[2]+'_featureImportanceTopTrain'
        os.system(train)
        pred='/usr/local/bin/python2.7 ../resources/parse_getID4matrixEx.py '+'%s'%sys.argv[2]+'_featureImportanceTop'+'%s'%sys.argv[8]+' '+'%s'%sys.argv[4]+' '+'%s'%sys.argv[4]+'_featureImportanceTopPred'
        os.system(pred)
        trainType='/usr/local/bin/python2.7 ../resources/addType.py '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[2]+'_featureImportanceTopTrain'+' '+'%s'%sys.argv[2]+'_featureImportanceTopTrainType'
        os.system(trainType)
        #predType='/usr/local/bin/python2.7 ../resources/addType.py '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[4]+'_featureImportanceTopPred'+' '+'%s'%sys.argv[4]+'_featureImportanceTopPredType'
        #os.system(predType)
        elsa='/usr/local/bin/python2.7 ../resources/run_elsa.py -t '+'%s'%sys.argv[2]+'_featureImportanceTopTrainType'+' -p '+'%s'%sys.argv[4]+'_featureImportanceTopPred'+' -o '+'%s'%sys.argv[10]
        os.system(elsa)
	subCell1='/usr/local/bin/python2.7 ../resources/extractTrainCell.py '+'%s'%sys.argv[2]+'_addType'+' '+'%s'%sys.argv[2]+' '+'%s'%sys.argv[12]+' '+'%s'%sys.argv[2]+'_sub'+' '+'%s'%sys.argv[10]+' '+'%s'%sys.argv[4]+' '+'%s'%sys.argv[4]+'_sub'
	#print subCell1
	os.system(subCell1)
	addTypeSub='/usr/local/bin/python2.7 ../resources/addType.py '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[2]+'_sub'+' '+'%s'%sys.argv[2]+'_subType'
	os.system(addTypeSub)
	featureSelectionSub='/usr/local/bin/python2.7 ../resources/feature_selection_RF.py '+'%s'%sys.argv[2]+'_subType'+' '+'%s'%sys.argv[2]+'_subType_featureImportance'
	os.system(featureSelectionSub)
	featureSortSub='sort -k 2 -r -g '+'%s'%sys.argv[2]+'_subType_featureImportance >'+'%s'%sys.argv[2]+'_subType_featureImportanceSort'
        os.system(featureSortSub)
        featureTopSub='head -n 20'+' '+'%s'%sys.argv[2]+'_subType_featureImportanceSort >'+'%s'%sys.argv[2]+'_subType_featureImportanceTop10'
        os.system(featureTopSub)
        trainSub='/usr/local/bin/python2.7 ../resources/parse_getID4matrixEx.py '+'%s'%sys.argv[2]+'_subType_featureImportanceTop10'+' '+'%s'%sys.argv[2]+'_sub'+' '+'%s'%sys.argv[2]+'_subType_featureImportanceTop10Train'
        os.system(trainSub)
        predSub='/usr/local/bin/python2.7 ../resources/parse_getID4matrixEx.py '+'%s'%sys.argv[2]+'_subType_featureImportanceTop10'+' '+'%s'%sys.argv[4]+'_sub'+' '+'%s'%sys.argv[4]+'_subType_featureImportanceTop10Pred'
        os.system(predSub)
        trainTypeSub='/usr/local/bin/python2.7 ../resources/addType.py '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[2]+'_subType_featureImportanceTop10Train'+' '+'%s'%sys.argv[2]+'_subType_featureImportanceTop10TrainType'
        os.system(trainTypeSub)
        #predTypeSub='/usr/local/bin/python2.7 ../resources/addType.py '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[4]+'_subType_featureImportanceTop10Pred'+' '+'%s'%sys.argv[4]+'_subType_featureImportanceTop10PredType'
        #os.system(predTypeSub)
	elsaSub='/usr/local/bin/python2.7 ../resources/run_elsa.py -t '+'%s'%sys.argv[2]+'_subType_featureImportanceTop10TrainType'+' -p '+'%s'%sys.argv[4]+'_subType_featureImportanceTop10Pred'+' -o '+'%s'%sys.argv[10]+'subType'
        os.system(elsaSub)
	elsaMerg='/usr/local/bin/python2.7 ../resources/confusionMatrix.py '+'%s'%sys.argv[10]+' '+'%s'%sys.argv[10]+'subType'+' '+'%s'%sys.argv[10]+'MergeType'
        os.system(elsaMerg)
	
	
	


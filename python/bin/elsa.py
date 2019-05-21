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
#' @example
#' python2.7, /usr/local/bin/python2.7 elsa.py parameters

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

Usage: python elsa.py classification scell/snuc/bulk [-m] [-i] [-g] [-o] [-s]
       python elsa.py projection     scell/snuc/bulk [-t] [-p] [-c] [-g] [-o] [-s]

classification arguments:
  -m, --cell_marker       	list for cell marker
  -i, --input_file        	input data for classification
  -g, --geneNum           	number of top importances
  -o, --output            	output file for cell types
  -s, --specify (optional)      specific cell type for extend, for example -s CD4:CD8

projection arguments:
  -t, --traning           	traning prep data
  -p, --prediction        	prediction prep data
  -c, --cell_type         	cell type list
  -g, --geneNum           	number of top importances
  -o, --output            	output file for cell types
  -s, --specify (optional)      specific cell type for t cell

"""

###################################

#Run classification job

if len(sys.argv) == 11:
  if 'classification' in sys.argv[1]:
    if 'scell' in sys.argv[2] or 'snuc' in sys.argv[2]:
      trainSelectList='/usr/local/bin/python2.7 ../resources/trainSelfTestSC.py '+'%s'%sys.argv[4]+' '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[6]+'_trainList'
      os.system(trainSelectList)
      trainSelectEx='/usr/local/bin/python2.7 ../resources/getCell.py '+'%s'%sys.argv[6]+'_trainList '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[6]+'_train'+' '+'%s'%sys.argv[6]+'_test'
      os.system(trainSelectEx)
      elsa='/usr/local/bin/python2.7 ../resources/caml_pip.py '+'-t '+'%s'%sys.argv[6]+'_train'+' -p '+'%s'%sys.argv[6]+'_test'+' -c '+'%s'%sys.argv[6]+'_trainList'+' -g '+'%s'%sys.argv[8]+' -o '+'%s'%sys.argv[10]
      os.system(elsa)

    if 'bulk' in sys.argv[2]:
      trainSelectList='/usr/local/bin/python2.7 ../resources/trainSelfTestBulk.py '+'%s'%sys.argv[4]+' '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[6]+'_trainList'
      os.system(trainSelectList)
      trainSelectEx='/usr/local/bin/python2.7 ../resources/getCell.py '+'%s'%sys.argv[6]+'_trainList '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[6]+'_train'+' '+'%s'%sys.argv[6]+'_test'
      os.system(trainSelectEx)
      elsa='/usr/local/bin/python2.7 ../resources/caml_pip.py '+'-t '+'%s'%sys.argv[6]+'_train'+' -p '+'%s'%sys.argv[6]+'_test'+' -c '+'%s'%sys.argv[6]+'_trainList'+' -g '+'%s'%sys.argv[8]+' -o '+'%s'%sys.argv[10]
      os.system(elsa)

if len(sys.argv) == 13:
  if 'classification' in sys.argv[1]:
    if 'scell' in sys.argv[2] or 'snuc' in sys.argv[2]:
      trainSelectList='/usr/local/bin/python2.7 ../resources/trainSelfTestSC.py '+'%s'%sys.argv[4]+' '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[6]+'_trainList'
      os.system(trainSelectList)
      trainSelectEx='/usr/local/bin/python2.7 ../resources/getCell.py '+'%s'%sys.argv[6]+'_trainList '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[6]+'_train'+' '+'%s'%sys.argv[6]+'_test'
      os.system(trainSelectEx)
      elsa='/usr/local/bin/python2.7 ../resources/caml_pip.py '+'-t '+'%s'%sys.argv[6]+'_train'+' -p '+'%s'%sys.argv[6]+'_test'+' -c '+'%s'%sys.argv[6]+'_trainList'+' -g '+'%s'%sys.argv[8]+' -o '+'%s'%sys.argv[10]+' -s '+'%s'%sys.argv[12]
      os.system(elsa)

    if 'bulk' in sys.argv[2]:
      trainSelectList='/usr/local/bin/python2.7 ../resources/trainSelfTestBulk.py '+'%s'%sys.argv[4]+' '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[6]+'_trainList'
      os.system(trainSelectList)
      trainSelectEx='/usr/local/bin/python2.7 ../resources/getCell.py '+'%s'%sys.argv[6]+'_trainList '+'%s'%sys.argv[6]+' '+'%s'%sys.argv[6]+'_train'+' '+'%s'%sys.argv[6]+'_test'
      os.system(trainSelectEx)
      elsa='/usr/local/bin/python2.7 ../resources/caml_pip.py '+'-t '+'%s'%sys.argv[6]+'_train'+' -p '+'%s'%sys.argv[6]+'_test'+' -c '+'%s'%sys.argv[6]+'_trainList'+' -g '+'%s'%sys.argv[8]+' -o '+'%s'%sys.argv[10]+' -s '+'%s'%sys.argv[12]
      os.system(elsa)    


###################################


#Run projection job

if len(sys.argv) == 13:
  if 'projection' in sys.argv[1]:
    elsa='/usr/local/bin/python2.7 ../resources/caml_pip.py '+'-t '+'%s'%sys.argv[4]+' -p '+'%s'%sys.argv[6]+' -c '+'%s'%sys.argv[8]+' -g '+'%s'%sys.argv[10]+' -o '+'%s'%sys.argv[12]
    #print caml
    os.system(elsa)
if len(sys.argv) == 15:
  if 'projection' in sys.argv[1]:
    elsa='/usr/local/bin/python2.7 ../resources/caml_pip.py '+'-t '+'%s'%sys.argv[4]+' -p '+'%s'%sys.argv[6]+' -c '+'%s'%sys.argv[8]+' -g '+'%s'%sys.argv[10]+' -o '+'%s'%sys.argv[12]+' -s '+'%s'%sys.argv[14]
    #print caml
    os.system(elsa)


###################################





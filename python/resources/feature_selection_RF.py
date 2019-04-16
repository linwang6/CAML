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
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier


trainFile=open(sys.argv[1],'r')#The traning file
output=open(sys.argv[2],'w')#The output file


exLtrain=[]
exMtrain=[]
cellTypesTrain=[]
geneName=[]

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
    if 'ypes' in line:
        for j in range(0,int(len(lineE))-1):
            geneName.append(lineE[j])


cellTypesTrain = np.array(cellTypesTrain)
exMtrain = np.array(exMtrain)
geneName = np.array(geneName)

X, y = exMtrain, cellTypesTrain
#X.shape
#clf = ExtraTreesClassifier(n_estimators=100)
clf = RandomForestClassifier(n_estimators=50)
clf = clf.fit(X, y)
imp = clf.feature_importances_
#model = SelectFromModel(clf, prefit=True)
#X_new = model.transform(X)
#X_new.shape

for i in range(0,int(len(geneName))):
    print >>output,geneName[i],clf.feature_importances_[i]


trainFile.close()
output.close()


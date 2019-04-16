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

import os
import re
import sys


markerL=open(sys.argv[1],'r')#marker list, which used in train_MarkerCheck.R 
cellType=open(sys.argv[2],'r')#cell type list
normTrEx1=open(sys.argv[3],'r')#normalized scRNA-Seq from train_MarkerCheck.R
normTrEx2=open(sys.argv[3],'r')#normalized scRNA-Seq from train_MarkerCheck.R
trainD=open(sys.argv[4],'w')#ouput of training data


mkl=[]
mkls={}


for line in markerL:
    line=line.strip()
    line=line.split()
    for n in range(0,int(len(line))):
        mkl.append('"'+line[n]+'"')
        mkls['"'+line[n]+'"']='"'+line[n]+'"'

#extract cell type information

cellT={}
for line in cellType:
    line=line.strip()
    line=line.split()
    cellT[line[0]]=line[1]

#get normalization value
nte=[]#normalization value

for line in normTrEx1:
    line=line.strip()
    lineE=line.split()
    a=0
    if '"CCND1' in line:
        for n in range(0,int(len(lineE))):
                a=a+1
                if lineE[n] in mkls:
                    nte.append(a)


#getting the expression of markers genes
cellID=''
exp=''

for line in normTrEx2:
    line=line.strip()
    lineE=line.split()
    if '"CCND1' in line:
        for id in range(0,int(len(lineE))):
            if lineE[id] in mkls.keys():
                cellID=cellID+lineE[id]+'       '
        print >>trainD,cellID+' '+'"Cell_types"'
        cellID

    if '"CCND1' not in line:
        
        for value in nte:
            #print value,len(lineE)
            exp=exp+lineE[int(value)]+' '
        if lineE[0] in cellT.keys():
            print >>trainD,lineE[0]+'   '+exp+' '+cellT[lineE[0]]
            exp=''
        if lineE[0] not in cellT.keys():
            exp=''

markerL.close()
normTrEx1.close()
normTrEx2.close()
trainD.close()


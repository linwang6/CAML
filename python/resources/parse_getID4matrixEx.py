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

import os
import re
import sys


featureTop=open(sys.argv[1],'r')#top importances list, which generated from feature selection step
normTrEx1=open(sys.argv[2],'r')#normalized scRNA-Seq from train_MarkerCheck.R
normTrEx2=open(sys.argv[2],'r')#normalized scRNA-Seq from train_MarkerCheck.R
predD=open(sys.argv[3],'w')#ouput of matrix data


mkl=[]
mkls={}


for line in featureTop:
    line=line.strip()
    line=line.split()
    mkl.append(line[0])
    mkls[line[0]]=line[0]

#extract cell type information


#get normalization value
nte=[]#normalization value

for line in normTrEx1:
    line=line.strip()
    lineE=line.split()
    a=0
    if '"' in lineE[1]:
        for n in range(0,int(len(lineE))):
                a=a+1
                if lineE[n] in mkls:
                    nte.append(a)


#getting the expression of top important genes
cellID=''
exp=''

for line in normTrEx2:
    line=line.strip()
    lineE=line.split()
    if '"' in lineE[1]:
        for id in range(0,int(len(lineE))):
            if lineE[id] in mkls.keys():
                cellID=cellID+lineE[id]+'       '
        print >>predD,cellID
        cellID

    if '"' not in lineE[1]:
        
        for value in nte:
            #print value,len(lineE)
            exp=exp+lineE[int(value)]+' '
        
        print >>predD,lineE[0]+'        '+exp
        exp=''
        

featureTop.close()
normTrEx1.close()
normTrEx2.close()
predD.close()



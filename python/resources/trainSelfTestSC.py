#coding=utf-8
#' Please cite our paper if our paper or code helped you.

import os
import re
import sys
from statistics import mean
import operator


markFile=open(sys.argv[1],'r')#markers.list, format, NK:"NCAM1";"FCGR3A
#normTrEx1=open(sys.argv[2],'r')#normalized scRNA-Seq from train_MarkerCheck.R
#normTrEx2=open(sys.argv[2],'r')#normalized scRNA-Seq from train_MarkerCheck.R
predD=open(sys.argv[3],'w')#ouput of cell type data


def getTop(mkl, mkls):
    normTrEx1=open(sys.argv[2],'r')
    normTrEx2=open(sys.argv[2],'r')
    nte=[]#normalization value
    totalNumber=0
    for line in normTrEx1:
        line=line.strip()
        lineE=line.split()
        a=0
        if '"' in lineE[1]:
                for n in range(0,int(len(lineE))):
                        a=a+1
                        if lineE[n] in mkls:
                                nte.append(a)
                #print nte
#getting the expression of top important genes
    cellID=''
    exp=''
    Ex=[]
    for line in normTrEx2:
        line=line.strip()
        lineE=line.split()
        totalNumber=totalNumber+1
        if '"' in lineE[1]:
                for id in range(0,int(len(lineE))):
                        if lineE[id] in mkls.keys():
                                cellID=cellID+lineE[id]+'       '
                Ex.append(cellID)
                cellID=''

        if '"' not in lineE[1]:
                for value in nte:
                        #print value,len(lineE)
                        exp=exp+lineE[int(value)]+'     '        
                Ex.append(lineE[0]+'    '+exp)
                #print lineE[0]+'       '+exp
                exp=''
    #print totalNumber
    return(totalNumber,Ex)
    normTrEx1.close()
    normTrEx2.close()

remDup={}
for line in markFile:
    line=line.strip()
    lineE=line.split(':')
    mkl=[]
    mkls={}
    for num in range(0,int(len(lineE[1].split(';')))):
        mkl.append(lineE[1].split(';')[num])
        mkls[lineE[1].split(';')[num]]=lineE[1].split(';')[num]
    iterms=getTop(mkl, mkls)

    limit=(int(iterms[0])-1)*0.02##single cell
    #print limit
    #limit=(int(iterms[0])-1)*0.1##bulk RNA-Seq
    alliterm={}
    aa=0
    sum=0
    for it in iterms[1]:
      its=it.split()
      if int(len(its))>1:
        if '"' not in its[1]:
            for k in range(1,int(len(its))):
                sum=sum+float(its[k])
            #print sum
            #if sum>0.0:
            alliterm[its[0]]=sum/(int(len(its))-1+0.00)
            sum=0
    alliterms=sorted(alliterm.items(), key=operator.itemgetter(1),reverse=True)
    #print alliterms
    
    for term in alliterms:
        aa=aa+1
        if aa<limit:
            
            if term[0] in remDup.keys():
                del remDup[term[0]]
            else:
                remDup[term[0]]=lineE[0]+' '+'%f'%term[1]

for finalIterm in remDup:
    print >>predD,finalIterm,remDup[finalIterm]


markFile.close()
predD.close()


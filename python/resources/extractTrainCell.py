import os
import re
import sys


trainType=open(sys.argv[1],'r')#training file with label
trainF=open(sys.argv[2],'r')#training file 
typesList=sys.argv[3]#typesList, e.g CD4;CD8
subFileTrain=open(sys.argv[4],'w')#output
preCellType=open(sys.argv[5],'r')#Predicted cell type file
preCellEx=open(sys.argv[6],'r')#Predicted expression file
subFilePred=open(sys.argv[7],'w')#output


typeL=[]
type=typesList.split(':')
#print type
for num in range(0,int(len(type))):
    typeL.append(type[num])


trainList=[]
for line in trainType:
    line=line.strip()
    lineE=line.split()
    if lineE[-1] in typeL:
        trainList.append(lineE[0])

for line in trainF:
    line=line.strip()
    lineE=line.split()
    if '"' in lineE[1]:
        print >>subFileTrain,line
    if lineE[0] in trainList:
        print >>subFileTrain,line

predList=[]
for line in preCellType:
    line=line.strip()
    lineE=line.split()
    if int(len(lineE))>2:
        if lineE[-1] in typeL:
            #print lineE[0]
            predList.append(lineE[0])

for line in preCellEx:
    line=line.strip()
    lineE=line.split()
    if '"' in lineE[1]:
        print >>subFilePred,line
    if lineE[0] in predList:
        print >>subFilePred,line


trainF.close()
subFileTrain.close()
preCellType.close()
preCellEx.close()
subFilePred.close()



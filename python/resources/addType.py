#!/usr/bin/python
import re
import sys
import os
import random

input1=open(sys.argv[1],'r')
input2=open(sys.argv[2],'r')
output=open(sys.argv[3],'w')

s=[]
t={}
for line in input1:
    line=line.strip()
    lineE=line.split()
    t[lineE[2]]=lineE[3]

for line in input2:
    line=line.strip()
    lineE=line.split()
    if '"' in lineE[1]:
        print >>output,line+'   '+'"Types"'
    if '"' not in lineE[1]:
        print >>output,line+'   '+t[lineE[0]]
   
input1.close()
input2.close()
output.close()



import re
import sys
import os
import random

input1=open(sys.argv[1],'r')
input2=open(sys.argv[2],'r')
output3=open(sys.argv[3],'w')
output4=open(sys.argv[4],'w')


s=[]
t={}
for line in input1:
    line=line.strip()
    lineE=line.split()
    if '"' not in lineE[3]:
        t[lineE[2]]=lineE[3]

for line in input2:
    line=line.strip()
    lineE=line.split()
    if '"' in lineE[1]:
        print >>output3,line##+'        '+'"Types"'
        print >>output4,line
    if '"' not in lineE[1]:
      if lineE[0] in t.keys():
        print >>output3,line#+' '+t[lineE[0]]
      if lineE[0] not in t.keys():
        print >>output4,line

input1.close()
input2.close()
output3.close()
output4.close()


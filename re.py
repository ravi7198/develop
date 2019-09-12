#!/usr/bin/python
import sys
oldKey=None
salesTotal=0
c=0
for line in sys.stdin:
    data=line.strip().split("\t")
    if len(data)!=2:
        continue
    thisKey,thisSale=data

    if oldKey and oldKey!=thisKey:
        print oldKey,"\t",salesTotal
        oldKey=thisKey;
        salesTotal=0
        c=0
    oldKey=thisKey
    salesTotal+=float(thisSale)
    c=c+1
if oldKey!=None:
    print oldKey,"\t",salesTotal

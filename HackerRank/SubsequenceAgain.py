#!/bin/python3
import sys
from collections import Counter
def newstr(s,d):
    
    for i in d:

        s = s.replace(i,"")
       
    return s
def subsequenceAgain(s, k):
    d = []
    count = Counter(s)
    
    for i in s:
        if( count[i]<k ):
            if(i not in d):
                d.append(i)
    return newstr(s,d)
    
if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())
    result = subsequenceAgain(s, k)
    print(result)
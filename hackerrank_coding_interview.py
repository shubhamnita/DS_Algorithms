#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxDiscount function below.
def maxDiscount(n, x, y, a, b):
    max_disc=0
    for i in range(1,n+1):
        if i%x==0 and i%y==0:
            max_disc+=max(a,b)
        elif(i%x==0):
            max_disc+=a
        elif(i%y==0):
            max_disc+=b
    return max_disc
if __name__ == '__main__':

#############################################################
#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the mutualSubstitutions function below.
def mutualSubstitutions(s, subFirst, subSecond):
    '''a={}
    for i in range(len(subFirst)):
        if subFirst[i] not in list(a.keys()):
            a[subFirst[i]]=subSecond[i]
            a[subSecond[i]]=subFirst[i]
        else:
            a.pop(subFirst[i],None)
    print(a)
    keys = list(a.keys())

    for i in range(len(s)):
        if s[i] in keys:
            print('charac->',s[i])
            s=s[:i]+a[s[i]]+s[i+1:]
            #s.replace(s[i],a[s[i]])
    return s
    '''
    
    for i in range(len(subFirst)):
        a={}
        a[subFirst[i]]=subSecond[i]
        a[subSecond[i]]=subFirst[i]

        for i in range(len(s)):
            if s[i] in list(a.keys()):
                #print('charac->',s[i])
                s=s[:i]+a[s[i]]+s[i+1:]                
    return s
if __name__ == '__main__':
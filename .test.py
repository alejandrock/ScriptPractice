#!/usr/bin/env python

import math

def sum(x,y):

   a = math.modf(x)
   b = math.modf(y)
   print(a[0]*b[0])
    

sum(5,5)
sum(5,4)
sum(5,3)


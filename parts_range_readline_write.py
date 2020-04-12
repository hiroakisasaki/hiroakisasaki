#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:45:19 2020

@author: hiroakisasaki
"""
f = open("./12girl", "r", encoding="utf-8")
o = open("out2.txt", "w", encoding="utf-8")

for i in range(10):
    doc = f.readline()
    o.write(doc)

import pdb; pdb.set_trace()    
    
f.close
o.close
    
    

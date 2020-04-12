#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:13:22 2020

@author: hiroakisasaki
"""

file = open("./12girl", "r", encoding="utf-8")
for i, line in enumerate(file):
    of = open('./out/{0:04d}'.format(i) + '.txt', 'w', encoding='utf-8')
    of.write(line)
    of.close()
file.close()
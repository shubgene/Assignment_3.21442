# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:26:36 2018

@author: shurastogi
"""
def subjectVerb():
    subjects=["Americans","Indians"]
    verbs=["play","watch"]
    objects=["Baseball","Cricket"]
    sentences=[(x+" "+y+" "+z) for x in subjects  for y in verbs for z in objects]
    for sen in sentences:
        print(sen)
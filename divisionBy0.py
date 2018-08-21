# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:17:35 2018

@author: shurastogi
"""
def divide5byNum(Num):
    try:
        return float(5/Num)
    except ZeroDivisionError as e:
        print("Please provide number greater than 0, Error is ",e)
    
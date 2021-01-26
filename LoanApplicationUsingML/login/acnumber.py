# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:23:52 2019

@author: aarus
"""


import random


def generate_acnumber(details):
    ac=str(int(random.random()*(10**8)))
    ac=ac+str(details['phno'])
    ac=int(ac)
    return ac    
    
    
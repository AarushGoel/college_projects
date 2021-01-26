# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:57:04 2019

@author: aarus
"""


def destroy_widgets_pack(parent):
     
    for e in parent.pack_slaves():
        print(e)
        e.destroy()



def destroy_widgets_place(parent):
     
    for e in parent.place_slaves():
        print(e)
        e.destroy()
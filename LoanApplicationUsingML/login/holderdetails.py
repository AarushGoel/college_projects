# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:30:10 2019

@author: aarus
"""
from bank_data import data


from tkinter import *

from destroy import *


#from user_page import UserPage



class AcDetials:
    
    
    def __init__(self,root,username):
        self.root=root
        self.username=username
        
        
    def load_account_details(self):
        
        
        acdetails=data.acDetails(self.username)
        
        destroy_widgets_pack(self.root)
        destroy_widgets_place(self.root)
        
        Label(self.root,text='Your Name :'+acdetails['name'],font=("Calibri", 13)).place(x=100,y=100)
        
        Label(self.root,text='Gender :'+acdetails['gender'],font=("Calibri", 13)).place(x=100,y=130)
        
        Label(self.root,text='Account Type :'+acdetails['actype'],font=("Calibri", 13)).place(x=100,y=160)
        
        Label(self.root,text='Address:'+acdetails['address'],font=("Calibri", 13)).place(x=100,y=190)
        
        Label(self.root,text='DOB:'+acdetails['dob'],font=("Calibri", 13)).place(x=100,y=210)
        
        Label(self.root,text='Account Balance:'+str(acdetails['acbalance']),font=("Calibri", 13)).place(x=100,y=240)
        
        
        Button(self.root,text='Back to User Page',font=("Calibri", 15),command=lambda:UserPage(self.root,self.username).load_user_page()).place(x=100,y=300)
        
        
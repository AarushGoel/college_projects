# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 02:10:29 2019

@author: aarus
"""



from tkinter import *

from destroy import *

from assistant import *

from holderdetails import *

from loan_approve import *

#from login_page import LoginPage

class UserPage:
    
    def __init__(self,root,username):
        self.root=root
        self.username=username
    
    
    def assist(self):
        obj_assist=Assistant(self.root,self.username)
        obj_assist.load_assistant_page()



    def deta(self):
        obj_deta=AcDetials(self.root,self.username)
        obj_deta.load_account_details()


    def loan_page(self):
        obj_loan=Loan_approve(self.root,self.username)
        obj_loan.load_loan_page()
        
        
    def loginpage(self):
        obj=LoginPage(self.root)
        obj.load_login_page()
        
        
    def load_user_page(self):
        
        destroy_widgets_pack(self.root)
        destroy_widgets_place(self.root)
            
        Button(self.root,text='Account Details',width="12", height="5",command=self.deta).place(x=220,y=50)
        
        Button(self.root,text='Loan Approval',width="12", height="5",command=self.loan_page).place(x=220,y=150)
        
        Button(self.root,text='Assistant',width="12", height="5",command=self.assist).place(x=220,y=250)
            
        
        Button(self.root,text='Log Out',width="10", height="5",command=self.loginpage).place(x=350,y=100)
    
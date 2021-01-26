# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:44:34 2019

@author: aarus
"""


from bank_data import data

from tkinter import *

from tkinter import messagebox

from user_page import *

from destroy import *

#from main_page import load_main_page

class LoginPage:
    
    def __init__(self,root):
        self.root=root
        self.username=None
        self.password=None
        
            
            
        
    def login_verify(self,user_entry,pass_entry):
        
        if user_entry.get()!='' and pass_entry.get()!='':
            self.username=user_entry.get()
            self.password=pass_entry.get()
        
        
    
            check=data.verify_login(self.username,self.password)
            
            if check==True:
                
                page=UserPage(self.root,self.username)
                page.load_user_page()
            else:
                
                messagebox.showerror('Error','Wrong Username or Password')
                
    def load_login_page(self):
        
    
        destroy_widgets_pack(self.root)
        destroy_widgets_place(self.root)
            
        user_label=Label(self.root,text="Username",width="300", height="2",font=("Calibri", 13))
        user_label.pack()
        
        user_entry=Entry(self.root)
        user_entry.pack()
        
        
        pass_label=Label(self.root,text="Password",width="300", height="2",font=("Calibri", 13))
        pass_label.pack()
        
        pass_entry=Entry(self.root,show="*")
        pass_entry.pack()
        
            
        login_but=Button(self.root,text="Login",width="5", height="1",command=lambda:self.login_verify(user_entry,pass_entry))
        login_but.pack()
        
        
            
        login_but=Button(self.root,text="Back To Main Menu",width="15", height="1",command=lambda:load_main_page(self.root))
        login_but.pack()
       
       
        
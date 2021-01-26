# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 01:33:54 2019

@author: aarus
"""



from login_page import *

from sign_up_page import *


from tkinter import *

from destroy import *


def loginPage(root):
    
    
    login_obj=LoginPage(root)
    login_obj.load_login_page()

def signPage(root):
    
    
    sign_up_obj=SignUp(root)
        
    sign_up_obj.load_signup_page()


def load_main_page(root):
    
    destroy_widgets_pack(root)
    destroy_widgets_place(root)
    root.geometry("520x400+350+200")
    
    Button(root,text='Login',width="10", height="5",command=lambda:loginPage(root)).place(x=220,y=100)
    
    
    Button(root,text='SignUp',width="10", height="5",command=lambda:signPage(root)).place(x=220,y=200)
    
    
    
if __name__=="__main__":
    root=Tk()
    load_main_page(root)
    
    root.mainloop()
    
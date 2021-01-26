# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:54:33 2019

@author: aarus
"""

#Loan.predict_loan(140000,'60 months','teacher','3 years','OWN',1000000,'car')


from tkinter import *

from loan.loan import Loan

from sklearn.externals import joblib

from bank_data import data

from destroy import *

from user_page import *


class Loan_approve:
    
    
    def __init__(self,root,username): # we have to pass a object for main window
        self.root=root
        self.username=username
       
        
    def userpage():
        obj=UserPage(self.root,self.username)
        obj.load_user_page()
    def approval(self,loan_amt,term,profession,ex,home_status,income,purpose):
        
        
        
        try:
            loan_amt=int(loan_amt)
            
        except Exception as e:
            print(e)
            messagebox.showerror('Error','Enter Loan amount in Numbers')
        
        
        try:
            income=int(income)
            
        except Exception as e:
            print(e)
            messagebox.showerror('Error','Enter Annual Income in Numbers')
        
        
        
        
        
        if type(loan_amt) and type(income) is int:
            
            if term=='3 years':
                term='36 months'
            elif term=='5 years':
                term='60 months'
            
            approve_status=Loan.predict_loan(loan_amt,term,profession,ex,home_status,income,purpose)            
            
            
            if approve_status==True:
                approve_status='approved'
            else:
                approve_status='rejected'
                
            details={}
            
            details['username']=self.username  
            details['loan_amt']=loan_amt
            details['term']=term
            details['pro']=profession
            details['ex']=ex
            details['home']=home_status
            details['income']=income
            details['purpose']=purpose
            details['loan_status']=approve_status
            
            data.loan_table(details)            
            
            destroy_widgets_pack(self.root)
            destroy_widgets_place(self.root)
            
            if approve_status=='approved':
                Label(self.root,text='Your Loan has been Approved',font=("Calibri", 20)).place(x=100,y=100)
                Label(self.root,text='Contact to your Branch with\n Neccessary Documents',font=("Calibri", 20)).place(x=100,y=150)
                
                Button(self.root,text='Back to User Page',font=("Calibri", 15),command=lambda:UserPage(self.root,self.username).load_user_page()).place(x=100,y=300)
        
            else:
                Label(self.root,text='Your Loan has been Rejected',font=("Calibri", 20)).place(x=100,y=100)
                Label(self.root,text='Contact to your Branch for \n More Approvals',font=("Calibri", 20)).place(x=100,y=150)
                
                Button(self.root,text='Back to User Page',font=("Calibri", 15),command=lambda:userpage.place(x=100,y=300))
    
        
    def load_loan_page(self):
        destroy_widgets_pack(self.root)
        destroy_widgets_place(self.root)
        
        label_loan_amt=Label(self.root,text='Loan Amount :',font=("Calibri", 13))
        label_loan_amt.place(x=100,y=20)
        
        
        
        entry_loan_amt=Entry(self.root)
        entry_loan_amt.place(x=220,y=22)
        
        
        
        label_loan_term=Label(self.root,text='Loan Term :',font=("Calibri", 13))
        label_loan_term.place(x=100,y=50)
        
        term=StringVar()
        term.set('3 years')
        
        
        
        loan_term=OptionMenu(self.root,term,'3 years','5 years')
        loan_term.place(x=220,y=52)
        
        
        label_loan_profession=Label(self.root,text='Your Profession :',font=("Calibri", 13))
        label_loan_profession.place(x=100,y=80)
        
    
    
    
        emp_title=joblib.load('loan/lab_emp_title')
        list_profession=emp_title.classes_            
        
        profession=StringVar()
        profession.set(list_profession[0])
        
        loan_profession=OptionMenu(self.root,profession,*list_profession)
        loan_profession.place(x=220,y=82)
    
    
    
        label_loan_emp_ex=Label(self.root,text='Your Experience :',font=("Calibri", 13))
        label_loan_emp_ex.place(x=100,y=110)
        
    
    
    
        emp_ex=joblib.load('loan/lab_emp_len')
        
        list_ex=emp_ex.classes_            
        
        ex=StringVar()
        ex.set(list_ex[0])
        
        loan_emp_ex=OptionMenu(self.root,ex,*list_ex)
        loan_emp_ex.place(x=220,y=112)
        
        label_loan_home=Label(self.root,text='Home Status :',font=("Calibri", 13))
        label_loan_home.place(x=100,y=140)
        
    
    
    
        home=joblib.load('loan/lab_home')
        
        list_home=home.classes_            
        
        home_status=StringVar()
        home_status.set(list_home[0])
        
        loan_home=OptionMenu(self.root,home_status,*list_home)
        loan_home.place(x=220,y=142)
        
        
    
    
        label_annual_income=Label(self.root,text='Annual Income :',font=("Calibri", 13))
        label_annual_income.place(x=100,y=170)
        
        entry_annual_income=Entry(self.root)
        entry_annual_income.place(x=220,y=172)
        
        
        
        
    
        label_loan_purpose=Label(self.root,text='Purpose :',font=("Calibri", 13))
        label_loan_purpose.place(x=100,y=200)
        
    
    
    
        purpose=joblib.load('loan/lab_purpose')
        
        list_purpose=purpose.classes_            
        
        loan_purpose=StringVar()
        loan_purpose.set(list_purpose[0])
        
        loan_purpose_option=OptionMenu(self.root,loan_purpose,*list_purpose)
        loan_purpose_option.place(x=220,y=202)
        
    
        
        submit=Button(self.root,text='Submit',bd=10,bg='blue',fg='red',command=lambda :self.approval(entry_loan_amt.get(),term.get(),profession.get(),ex.get(),home_status.get(),entry_annual_income.get(),loan_purpose.get()))
        submit.place(x=210,y=270)
    
    
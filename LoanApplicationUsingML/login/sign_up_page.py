# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:00:05 2019

@author: aarus
"""



from email_module  import email_verify


from acnumber import generate_acnumber

from bank_data import data

import re
from tkinter import *
from tkinter import messagebox
from main_page import load_main_page


from destroy import *

class SignUp:
    
    def __init__(self,root):
        self.root=root
        
    
    def main_page(self):
          load_main_page(self.root)      
   
        
        
        
    
    def otp_verify(self,otp,real_otp,refid,details):
       
    
        if int(otp.get())==real_otp:
            
            acnumber=generate_acnumber(details)
            
            details['acnumber']=acnumber
            details['refid']=refid
            
            data.add_acholder(details)
            
            destroy_widgets_place(self.root)
            Label(self.root,text='Your Account is Successfully Created',font=("Calibri", 20)).place(x=0,y=100)
            
            Label(self.root,text='Contact to your Near Branch with Documents',font=("Calibri", 20)).place(x=0,y=150)
            
            ref='Your Reference ID is '+'"'+str(refid)+'"'
            Label(self.root,text=ref,font=("Calibri", 20)).place(x=0,y=200)
            
            Button(self.root,text='Login Page',bd=10,bg='blue',
                              fg='red',command=self.main_page).place(x=230,y=300)
        else:
            messagebox.showerror('Error','Enter Wrong OTP')
        
        
    def sign_up_verify(self,details):
       
        
        
        real_otp,refid=email_verify(details)
        
        message='A OTP sent to your mail enter that and proceed '
        mess=Label(self.root,text=message,font=("Calibri", 20))
        mess.place(x=0,y=100)
     
        message2='Your Mail : '+details['email']
        mess2=Label(self.root,text=message2,font=("Calibri", 20))
        mess2.place(x=0,y=150)
     
        
        
        label_otp=Label(self.root,text='Enter OTP',font=("Calibri", 15))
        label_otp.place(x=80,y=218)
        
       
        
        otp=Entry(self.root)
        otp.place(x=200,y=220)
        
        submit_otp=Button(self.root,text='Verify',command=lambda:SignUp.otp_verify(self,otp,real_otp,refid,details),bd=10,bg='blue',fg='red')
        submit_otp.place(x=220,y=260)
        
        resend_otp=Button(self.root,text='Resend OTP',command=lambda:SignUp.sign_up_veriy(self,details),bd=10,bg='blue',fg='red')
        resend_otp.place(x=220,y=310)
        
    def sign_up_submit(self,entry_name,entry_phno,entry_email,entry_DOB,male,female,
                       entry_address,list_actype,entry_username,entry_pass,
                       entry_repass,gender,ac):
        
        
        flag=0
        
        if entry_name.get() =='':
            
            messagebox.showerror('Error','Enter Name')
            
        elif entry_name.get().isalpha():
            name=entry_name.get()
            flag+=1    
            
            
        else:
            messagebox.showerror('Error','Only Alphabets in Name field')
            
        
        if entry_phno.get() =='':
            
            messagebox.showerror('Error','Enter Phone Number')
                
        
        elif entry_phno.get().isdecimal():
            phno=entry_phno.get()
            r=re.findall('\d{10}',phno)
            
            if len(''.join(r))==len(phno):
                phno=int(phno)
                flag+=1
            else:
                messagebox.showerror('Error','Enter vaild Phone Number')
            
        else:
            messagebox.showerror('Error','Enter only Numbers in PhNo. Field')
            
            
        if entry_email.get()=='':
            messagebox.showerror('Error','Enter Email')
            
        else:
            email=entry_email.get()
            
            r=re.findall('\w+@\w+[.]\w+',email)
            
            if len(''.join(r))!=len(email):
                messagebox.showerror('Error','Enter vaild Email')
            else:
                email=entry_email.get()
                flag+=1
                
                
        if entry_DOB.get()=='':
            messagebox.showerror('Error','Date of Birth')
        else:
            DOB=entry_DOB.get()
            r=re.findall('\d{2}/\d{2}/\d{4}',DOB)
      
            
            if len(''.join(r))==len(DOB):
                DOB=entry_DOB.get()
                flag+=1
            else:
                messagebox.showerror('Error','Enter vaild Format DOB')
        
        if str(gender.get())=='0':
            
            messagebox.showerror('Error','Fill Your Gender')
    
        elif str(gender.get())=='1':
            ge='male'
            flag+=1
        elif str(gender.get())=='2':
            ge='female'
            flag+=1
    
    
        
        if entry_address.get() =='':
            
            messagebox.showerror('Error','Enter Address')
        else:
            address=entry_address.get()
            flag+=1
    
        
        account_type=ac.get()
        
        if account_type!=None:
            flag+=1
    
    
        
        if entry_username.get()=='':
            
            messagebox.showerror('Error','Enter Username')
        else:
            
            username=entry_username.get()
            flag+=1
        if entry_pass.get()=='':
            
            messagebox.showerror('Error','Enter Password')
            
        if entry_repass.get()=='':
            messagebox.showerror('Error','Enter Re-Password')
            
            
        if entry_pass.get().isalnum() and entry_pass.get()==entry_repass.get() and len(entry_pass.get())>=8 :
            password=entry_pass.get()
            flag+=1
        else:
            messagebox.showerror('Error','Enter Right Password')
            
            
        if flag==9:
            global details
            details={'name':name,'phno':phno,'email':email,'dob':DOB,'gender':ge,
                 'address':address,'account_type':account_type,
                 'username':username,'password':password}
            
            
            destroy_widgets_place(self.root)
            SignUp.sign_up_verify(self,details)
            
        
    def load_signup_page(self):
        
        
        
        destroy_widgets_pack(self.root)
        destroy_widgets_place(self.root)
    
        label_name=Label(self.root,text='Name :',font=("Calibri", 13))
        label_name.place(x=100,y=10)
        
        
        entry_name=Entry(self.root,font=("Calibri", 13))
        entry_name.place(x=180,y=12)
        
        label_phno=Label(self.root,text='Ph NO :',font=("Calibri", 13))
        label_phno.place(x=100,y=40)
        
        entry_phno=Entry(self.root,font=("Calibri", 13))
        entry_phno.place(x=180,y=42)
        
        
        label_email=Label(self.root,text='Email ID :',font=("Calibri", 13))
        label_email.place(x=100,y=70)
        
        entry_email=Entry(self.root,font=("Calibri", 13))
        entry_email.place(x=180,y=72)
        
    
        
        label_DOB=Label(self.root,text='DOB:',font=("Calibri", 13))
        label_DOB.place(x=100,y=100)
    
        entry_DOB=Entry(self.root,font=("Calibri", 13))
        entry_DOB.place(x=180,y=102)
    
        
        gender=IntVar()
            
        label_gender=Label(self.root,text='Gender :',font=("Calibri", 13))
        label_gender.place(x=100,y=130)
        
        male=Radiobutton(self.root,text='Male',value=1,variable=gender)
        male.place(x=180,y=132)
        
        
        female=Radiobutton(self.root,text='Female',value=2,variable=gender)
        female.place(x=250,y=132)
        
        
        label_address=Label(self.root,text='Address:',font=("Calibri", 13))
        label_address.place(x=100,y=160)
        
        entry_address=Entry(self.root,font=("Calibri", 13))
        entry_address.place(x=180,y=162)
        
        
        label_actype=Label(self.root,text='Account Type:',font=("Calibri", 13))
        label_actype.place(x=100,y=190)
        
        
        ac=StringVar(self.root)
        ac.set('Saving A/c')
        
        list_actype=OptionMenu(self.root,ac,'Saving A/c','Current A/c','Joint A/c')
        list_actype.place(x=180,y=192)
        
        label_username=Label(self.root,text='UserName:',font=("Calibri", 13))
        label_username.place(x=100,y=220)
        
        entry_username=Entry(self.root,font=("Calibri", 13))
        entry_username.place(x=180,y=222)
        
        
        label_pass=Label(self.root,text='Password:',font=("Calibri", 13))
        label_pass.place(x=100,y=250)
        
        entry_pass=Entry(self.root,font=("Calibri", 13),show='*')
        entry_pass.place(x=180,y=252)
        
        
        label_repass=Label(self.root,text='Re-Pass:',font=("Calibri", 13))
        label_repass.place(x=100,y=280)
        
        entry_repass=Entry(self.root,font=("Calibri", 13),show='*')
        entry_repass.place(x=180,y=282)
        
        submit=Button(self.root,text='Submit',bd=10,bg='blue',fg='red',command=lambda:SignUp.sign_up_submit(self,entry_name,entry_phno,entry_email,entry_DOB,male,female,
                       entry_address,list_actype,entry_username,entry_pass,
                       entry_repass,gender,ac))
        submit.place(x=210,y=310)
        
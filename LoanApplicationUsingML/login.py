# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:06:56 2019

@author: aarus
"""

from tkinter import *
from tkinter import messagebox
import re

from email_module  import email_verify
from acnumber import generate_acnumber
from bank_data import data


from loan_approve import loan_approve_gui

from login_page import *




#
#
#def destroy_widgets_pack(parent):
#     
#    for e in parent.pack_slaves():
#        print(e)
#        e.destroy()
#
#
#
#def destroy_widgets_place(parent):
#     
#    for e in parent.place_slaves():
#        print(e)
#        e.destroy()
#        
        
        
def loan_page():
    global root
    loan_approve_gui(root)

def destory_signup_page():
    
    global root
    global entry_name
    global entry_phno
    global entry_email
    global entry_DOB
    global male
    global female
    global entry_address
    global list_actype
    global entry_username
    global entry_pass
    global entry_repass
    global submit

    list_widgets=[entry_name,entry_phno,entry_email,entry_DOB,male,
                  female,entry_address,list_actype,entry_username,
                  entry_pass,entry_repass,submit]    
    
    
    for e in list_widgets:
        e.destroy()


def login_verify():
    global root
    global user_entry
    global pass_entry
    check=data.verify_login(user_entry.get(),pass_entry.get())
    
    if check==True:
        
        destroy_widgets_pack(root)
        destroy_widgets_place(root)
        loan_page_obj=loan_approve_gui(root)
        loan_page_obj.gui()
        
    else:
        messagebox.showerror('Error','Wrong Username or Password')


def login_main_page():
    
    global root
    login_page_obj=LoginPage(root)
    login_page_obj.load_login_page()
    
#    global root    
#    global user_entry
#    global pass_entry
#    
#    destroy_widgets_pack(root)
#    destroy_widgets_place(root)
#        
#    user_label=Label(root,text="Username",width="300", height="2",font=("Calibri", 13))
#    user_label.pack()
#    
#    user_entry=Entry(root)
#    user_entry.pack()
#    
#    
#    pass_label=Label(root,text="Password",width="300", height="2",font=("Calibri", 13))
#    pass_label.pack()
#    
#    pass_entry=Entry(root,show="*")
#    pass_entry.pack()
#    
#    login_but=Button(root,text="Login",width="5", height="1",command=login_verify)
#    login_but.pack()
#    
#    
#    sign_but=Button(root,text="Sign Up",width="5", height="1",command=sign_up)
#    sign_but.pack()




root=Tk()

root.geometry("520x400+350+200")
login_main_page()


root.mainloop()



def otp_verify():
    global root
    
    global otp
    global real_otp
    global details
    if int(otp.get())==real_otp:
        
        acnumber=generate_acnumber(details)
        
        details['acnumber']=acnumber
        details['refid']=refid
        
        data.add_acholder(details)
        
        destroy_widgets_place(root)
        Label(root,text='Your Account is Successfully Created',font=("Calibri", 20)).place(x=0,y=100)
        
        Label(root,text='Contact to your Near Branch with Documents',font=("Calibri", 20)).place(x=0,y=150)
        
        ref='Your Reference ID is '+'"'+str(refid)+'"'
        Label(root,text=ref,font=("Calibri", 20)).place(x=0,y=200)
        
        login_page=Button(root,text='Login Page',bd=10,bg='blue',
                          fg='red',command=login_main_page)
        login_page.place(x=230,y=300)
    else:
        messagebox.showerror('Error','Enter Wrong OTP')

def sign_up_verify(details):
    global root
    
    global real_otp
    global refid
    
    real_otp,refid=email_verify(details)
    
    message='A OTP sent to your mail enter that and proceed '
    mess=Label(root,text=message,font=("Calibri", 20))
    mess.place(x=0,y=100)
 
    message2='Your Mail : '+details['email']
    mess2=Label(root,text=message2,font=("Calibri", 20))
    mess2.place(x=0,y=150)
 
    
    
    label_otp=Label(root,text='Enter OTP',font=("Calibri", 15))
    label_otp.place(x=80,y=218)
    
    global otp
    
    otp=Entry(root)
    otp.place(x=200,y=220)
    
    submit_otp=Button(root,text='Verify',command=otp_verify,bd=10,bg='blue',fg='red')
    submit_otp.place(x=220,y=260)
    
    resend_otp=Button(root,text='Resend OTP',command=lambda:sign_up_veriy(details),bd=10,bg='blue',fg='red')
    resend_otp.place(x=220,y=310)
    
    
def sign_up_submit():
    
    
    global root
    global entry_name
    global entry_phno
    global entry_email
    global entry_DOB
    global male
    global female
    global entry_address
    global list_actype
    global entry_username
    global entry_pass
    global entry_repass
    global gender
    global ac
    
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
        
        
        destroy_widgets_place(root)
        sign_up_verify(details)
        
        
def sign_up():
    
    
    

    global root
    global entry_name
    global entry_phno
    global entry_email
    global entry_DOB
    global male
    global female
    global entry_address
    global list_actype
    global entry_username
    global entry_pass
    global entry_repass
    global gender
    global ac
    global submit

    
    destroy_widgets_pack(root)

    label_name=Label(root,text='Name :',font=("Calibri", 13))
    label_name.place(x=100,y=10)
    
    
    entry_name=Entry(root,font=("Calibri", 13))
    entry_name.place(x=180,y=12)
    
    label_phno=Label(root,text='Ph NO :',font=("Calibri", 13))
    label_phno.place(x=100,y=40)
    
    entry_phno=Entry(root,font=("Calibri", 13))
    entry_phno.place(x=180,y=42)
    
    
    label_email=Label(root,text='Email ID :',font=("Calibri", 13))
    label_email.place(x=100,y=70)
    
    entry_email=Entry(root,font=("Calibri", 13))
    entry_email.place(x=180,y=72)
    

    
    label_DOB=Label(root,text='DOB:',font=("Calibri", 13))
    label_DOB.place(x=100,y=100)

    entry_DOB=Entry(root,font=("Calibri", 13))
    entry_DOB.place(x=180,y=102)

    
    gender=IntVar()
        
    label_gender=Label(root,text='Gender :',font=("Calibri", 13))
    label_gender.place(x=100,y=130)
    
    male=Radiobutton(root,text='Male',value=1,variable=gender)
    male.place(x=180,y=132)
    
    
    female=Radiobutton(root,text='Female',value=2,variable=gender)
    female.place(x=250,y=132)
    
    
    label_address=Label(root,text='Address:',font=("Calibri", 13))
    label_address.place(x=100,y=160)
    
    entry_address=Entry(root,font=("Calibri", 13))
    entry_address.place(x=180,y=162)
    
    
    label_actype=Label(root,text='Account Type:',font=("Calibri", 13))
    label_actype.place(x=100,y=190)
    
    
    ac=StringVar(root)
    ac.set('Saving A/c')
    
    list_actype=OptionMenu(root,ac,'Saving A/c','Current A/c','Joint A/c')
    list_actype.place(x=180,y=192)
    
    label_username=Label(root,text='UserName:',font=("Calibri", 13))
    label_username.place(x=100,y=220)
    
    entry_username=Entry(root,font=("Calibri", 13))
    entry_username.place(x=180,y=222)
    
    
    label_pass=Label(root,text='Password:',font=("Calibri", 13))
    label_pass.place(x=100,y=250)
    
    entry_pass=Entry(root,font=("Calibri", 13),show='*')
    entry_pass.place(x=180,y=252)
    
    
    label_repass=Label(root,text='Re-Pass:',font=("Calibri", 13))
    label_repass.place(x=100,y=280)
    
    entry_repass=Entry(root,font=("Calibri", 13),show='*')
    entry_repass.place(x=180,y=282)
    
    submit=Button(root,text='Submit',bd=10,bg='blue',fg='red',command=sign_up_submit)
    submit.place(x=210,y=310)
    

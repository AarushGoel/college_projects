# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:12:32 2019

@author: aarus
"""

import random
import smtplib
import datetime

def email_verify(details):
    
    otp=random.randint(100000,999999)
    
    ref=random.random()*100
    
    date=datetime.datetime.now()
    ref=str(date.day)+details['name']+str(details['phno'])+str(date.hour)+str(date.minute)
    
        
    text="""Thank You Sir/madam {name} for Opening Account with us 
            Your Reference Id {ref} to contact at your
            Near Branch 
            OTP for Verification : {otp}""".format(name=details['name'],
                                                    ref=ref,otp=otp)
    
    
    host='smtp.gmail.com'
    port=587
    username='testingpy2799@gmail.com'
    password='iambest123'
    
    
    conn=smtplib.SMTP(host,port)
    conn.ehlo()
    conn.starttls()
    conn.login(username,password)
    
    try:
        conn.sendmail(username,details['email'],text)
        conn.quit()
        return otp,ref
    except:
        return None
        
        
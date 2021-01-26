# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:26:42 2019

@author: aarus
"""



import pyttsx3 
import speech_recognition as sr

from tkinter import *

from bank_data import data

from destroy import *

from user_page import *


class Assistant:
    
    
    
    def __init__(self,root,username):
        
        self.root=root
        
        self.username=username        
        
        self.acdetails=data.acDetails(username)                
        
        self.engine=pyttsx3.init('sapi5')
        voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',voices[1].id)
        
        
        self.r=sr.Recognizer()
        
        self.r.energy_threshold=1000
        self.r.pause_threshold=0.5
        
        
        self.user=None
        self.assis=None
        
        
    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    def takecommand(self):
        
            
        with sr.Microphone() as source:
            
            print('listening....')
            audio=self.r.listen(source)
                    
        query=self.r.recognize_google(audio,language='en-in')
        print(query)
        
        return query
    
    
    
    def execute_query(self,query):
        
        query=query.lower()
        
        if 'username' in query:
            return "Your Username is "+self.acdetails['username']
        elif 'name' in query:
            return "Your Name is "+self.acdetails['name']
        elif 'address' in query:
            return "Your Address is "+self.acdetails['address']
        elif 'balance' in query:
            return "Your Balance is "+str(self.acdetails['acbalance'])
        elif 'email' in query:
            return "Your E-Mail is "+str(self.acdetails['email'])
        elif 'phone' in query:
            return "Your Phone Number is "+str(self.acdetails['phno'])
        elif 'birth' in query:
            return "Your Date of Birth is "+str(self.acdetails['dob'])
        elif 'account type' in query:
            return "Your Account Type is "+str(self.acdetails['actype'])
        elif 'gender' in query:
            return "Your gender is "+str(self.acdetails['gender'])
        elif 'loan status' in query:
            return "Your loan is "+str(data.loan_status(self.username))
        elif 'complaint' in query:
            return "Tell the complaint!!!!"
            
        else :
            return 'Wrong Command said it Again !!!!' 
            
            
    def record_complaint(self):
        
        query=self.takecommand()
        print('complaint function ')
        
        data.complaint(self.username,query)
        
        self.user.configure(state='normal')
        self.user.delete('1.0',INSERT)
        self.user.insert(INSERT,query)
        self.user.configure(state='disable')
        
        self.root.update()
        
        self.ass_output('Your complaint is regisetered in our Database')
        
    def start_assistant(self):
        starting_mssg="Hello !!! {name} \n How can I help You ????".format(name=self.acdetails['name'])
        
        
        self.ass_output(starting_mssg)
        
        
        
        
    def ass_output(self,text):
        
        self.assis.configure(state='normal')
        self.assis.delete('1.0',INSERT)
        self.assis.insert(INSERT,text)
        self.assis.configure(state='disable')
        self.root.update()
        self.speak(text)
        
        
        
        
    def user_input(self):
        
        query=self.takecommand()
        
        
        self.user.configure(state='normal')
        self.user.delete('1.0',INSERT)
        self.user.insert(INSERT,query)
        self.user.configure(state='disable')
        
        self.root.update()
       
        text=self.execute_query(query)
        if 'complaint' in text:
            
            self.ass_output(text)
            
            self.record_complaint()
        else:
                
            self.ass_output(text)
            
   
        
    def load_assistant_page(self):
        
        destroy_widgets_pack(self.root)
        destroy_widgets_place(self.root)
          
        Label(self.root,text='Voice Assistant',font=("Calibri", 15)).place(x=200,y=10)
        
        
        self.assis=Text(self.root,height=2,width=30,font=("Calibri", 15))
        self.assis.place(x=20,y=50)
        
        
        
        self.user=Text(self.root,height=2,width=30,font=("Calibri", 15))
        self.user.place(x=200,y=150)
        
        mic=Button(self.root,text='Start',font=("Calibri", 15),command=self.user_input)
        mic.place(x=230,y=250)
        
        
        
        Button(self.root,text='Back to User Page',font=("Calibri", 15),command=lambda:UserPage(self.root,self.username).load_user_page()).place(x=100,y=300)
        
        self.start_assistant()
        
        
        
#        
#root=Tk()
#
#root.geometry("520x400+350+200")
#obj=Assistant(root,'aarush123')
#obj.load_assistant_page()
#
#root.mainloop()
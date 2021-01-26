# -*- coding: utf-8 -*-


"""
Created on Thu Jul 18 20:27:45 2019

@author: aarus
"""


import pymysql 

class data:
    
    
    
    
    def connection():
        
        
        try:
            conn=pymysql.connect(host='localhost',user='root',password='iambest',db='bank_database')
            cur=conn.cursor()
            return conn,cur
        
        except Exception as e:
            print(e)
            
            
            
    def loan_table(details):
        try:
            
                
            conn,cur=data.connection()
            
            
            
            sqlquery="insert into loan_table(username,loan_amt,term,profession,\
            experience,home_status,income,purpose,loan_status) values('%s','%d','%s','%s','%s',\
            '%s','%d','%s','%s')"%(details['username'],details['loan_amt'],details['term'],details['pro'],
            details['ex'],details['home'],details['income'],details['purpose'],details['loan_status'])
            
            cur.execute(sqlquery)
            
            
            
            conn.commit() 
            
        except Exception as e:
            print("error in loan_table:",e)
        finally:
            conn.close()
            
    
        
     
    def complaint(username,query):
        
        
        try:
            
                
            conn,cur=data.connection()
            
            
            
            sqlquery="insert into complaint_table(username,complaint) values('%s','%s')"%(username,query)
            
            cur.execute(sqlquery)
            
            
            
            conn.commit() 
            
        except Exception as e:
            print(e)
        finally:
            conn.close()
        
    def loan_status(username):
        try:
            
                
            conn,cur=data.connection()
            
            
            
            sqlquery="select loan_status from loan_table where username='%s'"%(username)
            
            cur.execute(sqlquery)
            
            s=cur.fetchall()
            
        except Exception as e:
            print(e)
        finally:
            conn.close()
            return s[0][0]
        
        
        
        
        
    def acDetails(username):
        
        acdetails={}
        conn,cur=data.connection()
        
        try:
            sql="select * from acholder where username='%s'"%(username)
            
            cur.execute(sql)
            acdet=cur.fetchall()
            
            sql='show columns from acholder'
            
            cur.execute(sql)
            col=cur.fetchall()
            
            
            for i in range(len(col)):
                acdetails[col[i][0]]=acdet[0][i]
                
                
                
        finally:
            conn.close()
            del acdetails['password']
            
            return acdetails
        
        
        return None
        
        
        
    def add_acholder(details):
        try:
            
                
            conn,cur=data.connection()
            balance=0
            
            
            sqlquery="insert into acholder(username,email,acnumber,password,name,address,actype,gender,refid,\
            dob,acbalance,phno) values('%s','%s','%d','%s','%s','%s','%s','%s','%s','%s','%f','%d')"%(details['username'],
            details['email'],details['acnumber'],details['password'],details['name'],details['address'],details['account_type'],
            details['gender'],details['refid'],details['dob'],balance,int(details['phno']))
            
            cur.execute(sqlquery)
            
            
            
            conn.commit() 
            
        except Exception as e:
            print(e)
        finally:
            conn.close()
            
    def verify_login(username,entered_password):
        
        
        try:
            
            conn,cur=data.connection()
            
            sqlquery="select password from acholder where username='%s'"%(username)
            
            cur.execute(sqlquery)
            password=cur.fetchone()
            
        except Exception as e:
            print(e)
        finally:
                
            conn.close()
            try:
                if entered_password==password[0]:
                    return True
                
            except:
                return False
            
        
            
            
            
    
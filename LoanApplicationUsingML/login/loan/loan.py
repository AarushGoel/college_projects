# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:24:11 2019

@author: aarus
"""


import pandas as pd

import numpy as np

from sklearn.preprocessing import LabelEncoder


from sklearn.externals import joblib

from sklearn.tree import DecisionTreeClassifier



from sklearn.metrics import confusion_matrix
    
from sklearn.metrics import recall_score,f1_score,precision_score






class Loan:
    
    
    def predict_loan(loan_amnt,term,
                     emp_title,emp_length,
                     home_ownership,annual_inc,purpose):
        
        
        
        X_pred=[loan_amnt,term,
                     emp_title,emp_length,
                     home_ownership,annual_inc,purpose]
        df=pd.DataFrame(X_pred)
        df=df.T
        
        X_pred=df.iloc[:,:].values
        
        
        for i,k in zip([1,2,3,4,6],['lab_term','lab_emp_title','lab_emp_len','lab_home','lab_purpose']):
            
            lab=joblib.load('D:/minor_project/login/loan/'+k)
            X_pred[:,i]=lab.transform(X_pred[:,i])
            
        oh=joblib.load('D:/minor_project/login/loan/one_hot')
        X_pred=oh.transform(X_pred)
        X_pred=X_pred.toarray()
        
        
        dt=joblib.load('D:/minor_project/login/loan/dt_train')
        y_pred=dt.predict(X_pred)
        
        
        #return true means loan approved 
        #return false means loan not approved
        
        if y_pred==0:  
            return True
        elif y_pred==1:
            return False
        else:
            return None
    






if __name__=="__main__":
    
    dataset=pd.read_csv('train.csv')
    

    dataset=dataset.dropna(subset=['loan_amnt','term','grade',
                                   'emp_title','emp_length',
                                   'home_ownership','annual_inc','purpose'])
   
    dataset['emp_title'] = dataset['emp_title'].str.lower()    
    
    
    list_driver=['truck driver']
    
    list_nurse=['registered nurse']
    
    list_manager=['office manager','project manager',
                  'sales manager','general manager',
                  'operations manager','store manager',
                  'account manager','assistant manager',
                  'branch manager','program manager','it manager',
                  'regional manager','']
    
    
    
    dataset=dataset.replace(list_nurse,'nurse')
    
    dataset=dataset.replace(list_driver,'driver')
    
    dataset=dataset.replace(list_manager,'manager')
    
    l=dataset['emp_title'].value_counts()
    
    list1=[]
    
    for i in l.keys():
        if l[i]>=1980:
            list1.append(i)
    
 
    new_dataset=pd.DataFrame()
    
    for s in list1:
        print(s)
        new_dataset=new_dataset.append(dataset[dataset.emp_title ==s])
        
    dataset=new_dataset
    dataset=dataset[dataset.home_ownership !='ANY']
    
    X=dataset.iloc[:,[1,4,9,10,11,12,16]].values
    
    
    
    
    #converting into Inddian Currency
    
    for i in range(71979):
        X[i][0]=X[i][0]*10
        X[i][-2]=X[i][-2]*10
        
    
    lab=LabelEncoder()
    
    
    for i,k in zip([1,2,3,4,6],['lab_term','lab_emp_title','lab_emp_len','lab_home','lab_purpose']):
        X[:,i]=lab.fit_transform(X[:,i])    
        joblib.dump(lab,k)
        print(lab.classes_)
        
    
        
    
    y=dataset.iloc[:,[-1]].values
    
    
    
    from sklearn.preprocessing import OneHotEncoder
    oh=OneHotEncoder(categorical_features=[1,2,3,4,6])
    X=oh.fit_transform(X)
    X=X.toarray()
    joblib.dump(oh,'one_hot')
    
    dt=DecisionTreeClassifier(max_depth=60)
    
    dt.fit(X,y)
        
    y_pred=dt.predict(X)

    s=dt.score(X,y)
        
    cm=confusion_matrix(y,y_pred)
    r_score=recall_score(y,y_pred)
    p_score=precision_score(y,y_pred)
    f1=f1_score(y,y_pred)
        
    
    
    
    joblib.dump(dt,'dt_train')
    
    
    
    
    
    
    
    
        
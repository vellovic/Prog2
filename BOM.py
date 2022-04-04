# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:32:51 2022

@author: victo
"""
import time
import requests
import pandas as pd
import json

def get_data():
    status = 1
    sec = 0.2
    while status == 1:
        x = requests.get("http://160.85.252.148")
        time.sleep(sec)
        sec += 0.2
        if x.status_code != 500:
            status += 1
            print(x.text)
            return x.text
            

def clean_data():
    data = json.loads(get_data())
    df = pd.DataFrame(list(data.items()), columns = ['Item','Price'])
    clean = df[df['Price'].apply(lambda x: str(x).isdigit())]
    clean = clean.reset_index(drop = True)
    #print(len(clean['Item']))
    final = corrector(clean)
    
    print(final)
    print('Total:    ',final.sum(numeric_only = True))
    
   
    
    return final
    
    
 
    
 
def corrector(clean):
    old_values = []
    new_values = []
    i = 1
    for i in range(len(clean['Item'])):
        old_values.append(clean['Item'][i])
        #print(old_values)
        i =+ 1
    for items in range(len(old_values)):
        new_values.append(old_values[items].encode("windows-1252").decode("utf-8"))
        items =+ 1
        #print(new_values)
        
    return clean.replace(old_values, new_values )
    
    
data = clean_data()



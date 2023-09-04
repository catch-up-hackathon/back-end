# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 18:20:03 2023

@author: swann
"""
 
import pandas as pd
import os

path = os.path.join(os.getcwd(), 'db')
filename = 'db.csv'

def find_profil(data):
    
    ### db에서 사용자 아이디 확인 후 사용자 정보 출력
    
    user_id = data['user_id']
    user_data_base = pd.read_csv(os.path.join(path, filename))
    user_info = user_data_base[(user_data_base['id'] == user_id)]
    
    return user_info

def update_profil(data):
    
    ###사용자 건강 정보 업데이트
    
    user_id = data['user_id']
    db = pd.read_csv(os.path.join(path, filename), encoding='utf-8-sig')
    db[db['id']==user_id] =[user_id,
                            str(data.alergy),
                            data.diabet,
                            data.diet
                            ]
    
    db.to_csv(os.path.join(path, filename), encoding='utf-8-sig')
    print('user info update done')
    
    return True

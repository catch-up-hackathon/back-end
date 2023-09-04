# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 16:44:14 2023

@author: swann
"""

from flask import Flask, request
from recipe_extract import content
from profil import find_profil, update_profil
from api_search import get_product_info, get_product_info_one
import json


app = Flask(__name__)

@app.route('/')

@app.route('/test', methods = ['POST', 'GET'])
def test():
    #print('ok')
    print("get request.form:",request.form.to_dict())
    return 'ok'

@app.route('/url', methods = ['POST'])
def get_recipe():
    
    ###링크를 받아 어떤 플랫폼에 해당하는지 확인 후 해당 링크에서 레시피 정보를 갖고옴.  
    
    url = request.form.to_dict()
    url = url['url']
    temp = content(url)
    temp.extract(temp.platform)
    recipe = temp.make_recipe()
    
    return {"status" : True,
            "url" : url,
            "data" : recipe}
    


@app.route('/main', methods = ['POST', 'GET'])
def get_ingredient():
    
    ### 식재료당 해당하는 쇼핑몰 아이템 하나씩 갖고옴
    
    data = request.form.to_dict()
    ing = data['ingredients']
    ing = eval(ing)
    res = []
    
    for i in ing:
        name = i['name']
        try:
            res.append({"name":name,
                    "data": get_product_info_one(name)})
        except: 
            res.append({"name":name,
                       "data": {}})
    
    return res


@app.route('/order', methods = ["POST"])
def order():
    ###주문 함수 
    status = True
    data = request.form.to_dict()
    def orderfunction(data):#추후에 추가될 함수
        return True
    try:
        res = orderfunction(data)
        
    except:
        status = False
    return{"status":status,
           "data":res}
    
        
@app.route('/profile', methods = ['POST', 'GET'])
def profil_show():
    
    #마이페이지에서 보이는 유저정보
    
    status = False
    
    try:
        data = request.form.to_dict()

        try:
            profil_data = find_profil(data)
        except :
            print('user info not found')
            
    except:
        print('input data error')
        
    res = {"status": status,
           "data": profil_data}    
    return res

@app.route('/profile_update', methods = ['POST', 'GET'])
def profil_update():
    ### 유저 정보 업데이트
    try:
        data = request.form.to_dict()

    except:
        print('input data error')
        return False
    try:   
        update_profil(data)
    except:
        print('data update error')
        return False
    return True
    

@app.route('/login')
def login():
    return ''


@app.route('/replacement', methods = ['POST', 'GET'])
def replacement():
    ###장바구니에서 같은 종류의 다른 물건으로 바꾸는 기능
   
    
    data = request.form.to_dict()
    article = data['name']
     
    stuff = get_product_info(str(article))
      
    return type(stuff)

host_addr = "0. 0. 0. 0"





if __name__ == '__main__':
    app.run(debug=True)
    
    
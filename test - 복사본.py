# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 14:41:58 2023

@author: swann
"""


import requests
from bs4 import BeautifulSoup

def delete_iframe(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status() # 문제시 프로그램 종료
    
    soup = BeautifulSoup(res.text, "html.parser") 

    try: 
        url = "https://blog.naver.com/" + soup.iframe["src"]
    
    except:
        pass
    
    return url

def text_scraping(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status() # 문제시 프로그램 종료
    soup = BeautifulSoup(res.text, "html.parser") 

    if soup.find("div", attrs={"class":"se-main-container"}):
        text = soup.find("div", attrs={"class":"se-main-container"}).get_text()
        text = text.replace("\n","") #공백 제거
        print("done")
        return text
    elif soup.find("div", attrs={"class":"post_ct"}):
        text = soup.find("div", attrs={"class":"post_ct"}).get_text()
        text = text.replace("\n","") #공백 제거
        print("done")
        return text
    else:
        print("blog text extraction error")
        return False
        
    
#%%
# -*- coding: utf-8 -*-

# Sample Python code for youtube.captions.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = r'C:\Users\swjo\Desktop\python\ect\backend\client_secret_126623692855-h5hdor8uq1285ok49d3v70rdp8plq28c.apps.googleusercontent.com.json'
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.captions().list(
        part="id",
        videoId="iTIMT53NlF8"# exemple
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    #main()
    pass

    
if __name__ =="__main__":
    url = "https://evergreen22.tistory.com/entry/%EC%83%88%EC%BD%A4%EB%8B%AC%EC%BD%A4%EB%A7%9B%EC%9E%88%EB%8A%94-%ED%83%95%EC%88%98%EC%9C%A1-%EC%86%8C%EC%8A%A4-%EB%A7%8C%EB%93%A4%EA%B8%B0%EC%9D%B4%EC%97%B0%EB%B3%B5-%ED%83%95%EC%88%98%EC%9C%A1-%EB%A7%8C%EB%93%A4%EA%B8%B0"
    #url = delete_iframe(url)
    text =text_scraping(url)
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 11:06:32 2023

@author: swjo
"""

from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import re
import os
from googleapiclient.discovery import build
from google.oauth2 import credentials
import os
import google.auth
from google.oauth2.credentials import Credentials
from prompt import run_gpt
import json


api_key = "AIzaSyAvoEzNtkd3WlGQ2uTH770XcAGofarMLuA" ##임시 유튜브 api key
api_key = "AIzaSyDbjqltYui2_PbDT7EA0Dhy9lnERn6J6Qo"
youtube = build('youtube', 'v3', developerKey=api_key)
project_id = "norse-retina-397706"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
developer_key = "YOUR_DEVELOPER_KEY"
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # 테스트용
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

CLIENT_SECRET_FILE = 'client_secret_126623692855-h5hdor8uq1285ok49d3v70rdp8plq28c.apps.googleusercontent.com.json'
#C:\Users\swjo\Desktop\python\ect\backend



def extract_video_id(youtube_url):
    # YouTube 비디오 ID를 추출하는 정규표현식 패턴
    pattern = r"(?<=v=)[\w-]+(?=&|\s|$)"
    
    # 정규표현식을 사용하여 비디오 ID 추출
    match = re.search(pattern, youtube_url)
    
    if match:
        video_id = match.group(0)
        return video_id
    else:
        return None
    
def get_video_info(video_url):
    ###pytube를 이용하여 description 추출
    try:
        yt = YouTube(video_url)
        video_info = {
            "title": yt.title,
            "author": yt.author,
            "publish_date": yt.publish_date,
            "views": yt.views,
            "length": yt.length,
            "description": yt.description,
        }
        return video_info
    except Exception as e:
        return f"Error: {str(e)}"

def get_video_description(video_url):
    ###뷰티풀숲을 이용한 크롤링으로 description추출
    try:
        response = requests.get(video_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            description = soup.find('meta', {"name": "description"})["content"]
            return description
        else:
            return "Failed to fetch video description."
    except Exception as e:
        return f"Error: {str(e)}"
    
def get_video_captions(video_id):
    ###video id로 캡션 받기
    try:
        captions = youtube.captions().list(
            part='snippet',
            videoId=video_id
        ).execute()
        return captions
    except Exception as e:
        print(e)
        return None

def get_caption_script(caption_id):
    ###캡션id 로부터 자막 다운로드
    try:
        caption = youtube.captions().download(
            id=caption_id,
            tfmt='vtt'
        ).execute()
        return caption
    except Exception as e:
        print(e)
        return None
        
def delete_iframe(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    res = requests.get(url, headers=headers)
    #res.raise_for_status() # 문제시 프로그램 종료
    soup = BeautifulSoup(res.text, "html.parser") 
    try:
        src_url = "https://blog.naver.com/" + soup.iframe["src"]
    except:
        return url
    return src_url

def text_scraping_naver(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    res = requests.get(url, headers=headers)
    #res.raise_for_status() # 문제시 프로그램 종료
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

def text_scraping_tstory(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    res = requests.get(url, headers=headers)
    #res.raise_for_status() # 문제시 프로그램 종료
    soup = BeautifulSoup(res.text, "html.parser") 

    if soup.find("div", attrs={"class":"contents_style"}):
        text = soup.find("div", attrs={"class":"contents_style"}).get_text()
        text = text.replace("\n","") #공백 제거
        print("done")
        return text
    
    elif soup.find("div", attrs={"class":"entry-content"}):
        text = soup.find("div", attrs={"class":"entry-content"}).get_text()
        text = text.replace("\n","") #공백 제거
        print("done")
        return text
    else:
        print("blog text extraction error")
        return False

def get_platform(url)->True:
    """

    Parameters
    ----------
    url : str
        recipe url

    Returns
    -------
    True
        
    링크를 받아 어떤 플랫폼에 해당하는지 확인

    """
    if 'blog.naver.com' in url:
        platform = 'naver'
        print('naver link detected')
    
    elif '.tistory.com' in url:
        platform = 'tstory'
        print('tstory link detected')
        
    elif '.youtube.com' in url:
        platform = 'youtube'
        print('youtube link detected')
        
    else : 
        print('Url error')
        return False
    
    return platform

class content:
    def __init__(self, url):
        
        self.url = url
        self.platform = get_platform(self.url)
        self.data = {}
        
    def show(self):
        
        print({"url":self.url,
               "platform":self.platform,
               "data":self.data
                   })
        return True
    
    def extract(self, mode):
        
        ###링크에서 레시피 정보 추출
        
        if mode == 'youtube':
            
            
            
            ###유튜브 링크에서 description, script 추출
            
            video_url = self.url
            description = get_video_description(video_url)
            video_id = extract_video_id(self.url)
            if video_id:
                print(f"Extracted Video ID: {video_id}")
            else:
                print("Video ID not found in the URL.")
        
            if description:
                print("Video Description:")
                print(description)
            else:
                print("No description found.")
                
            
            video_script = ''
    
            
            """
            박선우님의 비디오 스크립트 추출 함수
            """
            
            
            
            self.data = {"video_description" :  description,
                         "video_script" : video_script}
            
            
            return True
    
        
    
        elif mode == 'naver':
            
            
            url = delete_iframe(self.url)   #네이버 블로그 특성상   ifram이 있을경우 제외
            text = text_scraping_naver(url) #블로그 본문 추출
            
            if text == False:
                
                return False
                
            else:
                self.data = {"content":text
                    }
            
            
            return True
        
        elif mode == 'tstory':
            
            content = text_scraping_tstory(self.url) #티스토리 본문 추출
            
            if content == False:
                return False
            
            self.data = {"data" : content
                }
           
            
            return True
        
    def make_recipe(self):
        ###크롤링 된 데이터에서 재료, 대체재, 정리된 레시피를 뽑아오는 코드
        if self.platform == 'naver' or 'tstory':
            context = self.data['content']
        elif self.platform == 'youtube':
            context = self.data['video_description'] + self.data['video_script']

        res = run_gpt()
        res_json = json.loads(res)
        return res_json
    


   

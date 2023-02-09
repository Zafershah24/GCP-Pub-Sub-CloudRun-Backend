import requests
import os

from bs4 import BeautifulSoup

os.environ['http_proxy'] = HTTP_PROXY
# os.environ['HTTP_PROXY'] = HTTP_PROXY
os.environ['https_proxy'] = HTTPS_PROXY
# os.environ['HTTPS_PROXY'] = HTTPS_PROXY
os.environ['NO_PROXY'] = NO_PROXY

def webexpush(recipient, subject,mss):
  apiUrl = 'https://webexapis.com/v1/messages'
  soup = BeautifulSoup(mss)
  mss=soup.get_text()
  access_token = ''
  httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token }
  subject=subject.upper()
  
  body = { 'toPersonEmail': recipient+'@ford.com', 'text':subject+'\n'+mss }
  response = requests.post( url = apiUrl, json = body, headers = httpHeaders )
    

  

  print( response.status_code )
  print( response.text )

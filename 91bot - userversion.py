
# -*- coding: utf-8 -*-


from urllib import urlretrieve
import requests
from bs4 import BeautifulSoup
import re

headers={
"cookie":"" #你自己的91cookie
"Connection":"keep - alive",
"Upgrade - Insecure - Requests":"1",
"Cache - Control":"max - age = 0",
"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0",
"Referer":"http://91.91p09.space/v.php?next=watch"
}

url=raw_input(u'请输入91视频网址：')
req=requests.get(url.strip(),headers=headers)
soup=BeautifulSoup(req.text)
name=soup.select('#viewvideo-title')[0].get_text().strip()
videourl=str(soup.select('div[class="example-video-container"] > video > source')[0]).split('"')[1]
name='E:\\pyworkspace\\re\\91\\'+'%s.mp4'%name
print videourl,name
urlretrieve(videourl,name)
print 'Downloading Finished!'

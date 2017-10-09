#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date : 
# @Author : Changning Yang (thevile@126.com)
import http.cookiejar
from urllib2 import build_opener,HTTPCookieProcessor
from urllib import urlencode
import random
import re
import time
import json
import csv
import sys

agentPool = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
class dj():

    def __init__(self):
        # -----BASEURL  为目标网站的URL
        # -----ToSearchJob  为需要搜寻的工作
        # -----Agent  为Agent池，用于伪装浏览器
        # -----opener 为自己建造的一个opener，配合cookiejar可用于存储cookies
        def Myopener(self):
                cookie = http.cookiejar.CookieJar()
                return build_opener(HTTPCookieProcessor(cookie))

        self.BASEURL = "https://www.dajie.com/"
        # self.ToSearchJob=Jobs.TheJobNeedToSearch
        self.AgentPool = agentPool

        self.opener = Myopener(self=self)

        pass

    def getContext(self,page,keyword):
        url="https://so.dajie.com/job/search?keyword=%E7%A8%8B%E5%BA%8F%E5%91%98&from=job"

        header=\
            {
                "User-Agent":random.choice(agentPool),
                "Referer":"https://so.dajie.com/job/search?keyword=%E7%A8%8B%E5%BA%8F%E5%91%98&from=job"
            }

        head=[]

        for key,value in header.items():
            head.append((key,value))

        self.opener.addheaders=head

        #session_cookie用于保存服务器返回的cookie，并将其保存
        #
        #其实只需要保存  session_cookie["SO_COOKIE_V2"]  即可，其余的是多余的。服务器在进行验证的时候，只会验证 SO_COOKIE_V2
        #
        session_cookie={}
        session=self.opener.open("https://so.dajie.com/job/search?keyword=%E7%A8%8B%E5%BA%8F%E5%91%98&from=job")

        session_cookie["DJ_RF"]= re.findall(r"DJ_RF=.+?;",str(session.info()))[0].split("=")[1]
        session_cookie["DJ_EU"]=re.findall(r"DJ_EU=.+?;",str(session.info()))[0].split("=")[1]
        session_cookie["DJ_UVID"] = re.findall(r"DJ_UVID=.+?;", str(session.info()))[0].split("=")[1]
        session_cookie["SO_COOKIE_V2"] = re.findall(r"SO_COOKIE_V2=.+?;", str(session.info()))[0].split("=")[1]

        #data 包含的是所需要传入的 cookie
        data=\
            {
                "DJ_RF":session_cookie["DJ_RF"].strip(";"),
                "DJ_EU":session_cookie["DJ_EU"].strip(";"),
                "DJ_UVID":session_cookie["DJ_UVID"].strip(";"),
                "SO_COOKIE_V2":session_cookie["SO_COOKIE_V2"].strip(";"),
                "__login_tips":1,
            }
        #将 数据解析为传入数据的格式
        _data=urlencode(data,"utf-8")

        #
        #_url 指的是ajax的链接地址
        _url="https://so.dajie.com/job/ajax/search/filter?keyword=%s&order=0&city=&recruitType=&salary=&experience=&page=%d&positionFunction=&_CSRFToken=ZGbqQR9Ge43kyqBmnRpiL_caXgFsoBoJf1vTMSqk&ajax=1"%(keyword,page)
        req=self.opener.open(_url,data=_data.encode("utf-8"))


        return req.read().decode("utf-8")


        #print(req.read().decode("utf-8"))



if __name__=="__main__":
    reload(sys)
    sys.setdefaultencoding('gbk')
    kd=['python','java','c++','php','android']

    for i in kd:
        _dj=dj()
        content = json.loads(_dj.getContext(1,i).encode('unicode-escape').decode('string_escape'))
        pc=int(content['data']['totalPage'])
        csvf=file('%s.csv'%i,'wb')
        writer =csv.writer(csvf)
        writer.writerow(['jobtype','jobname','companyname','salary','location'])
        for pn in range(1,pc+1):
            _dj=dj()
            data=[]
            try:
                content = _dj.getContext(pn, i).encode('unicode-escape').decode('string_escape','ignore')
                content = json.loads(content)
                for each in content['data']['list']:
                    data.append((i,each['jobName'],each['compName'],each['salary'],each['pubCity']))
                writer.writerows(data)
                time.sleep(random.uniform(0,2))
            except:
                pass
        csvf.close()
        print i,' finished!'


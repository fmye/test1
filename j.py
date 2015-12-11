# -*- coding: utf-8 -*-
import sys
import re

from HTMLParser import HTMLParser
import urllib2
import cookielib
import urllib
import cookielib

## 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")
#####################################################
#登录人人
value_list = ["asset-value", "asset-amt", "asset-all", "date", "price", "amt", "amt-vaue", "scale", "risk", "subscribe-status","redeem-status"]

loginurl = 'http://www.jisilu.cn/login/'
logindomain = 'jisilu.cn'
class FundDataParser(HTMLParser):
    def __init__(self, value_list = value_list):
        HTMLParser.__init__(self) # old-style class could not use super
        self._process = False
        self.value_list =  value_list
        self.attr = ""
        self.data = {}
        self.result = {}

    def get(self, code):
        url = "http://www.jisilu.cn/data/sfnew/#tlink_3"
        f = urllib2.urlopen(url)
        html = f.read()
        print html
        self.feed(html)
        self.close()
        self.result = self.data
        self.data = {}
        return(self.result)

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for attr in attrs:
                if (attr[0] == "class"):
                    # case <span class="asset-amt red">
                    for attr_name in attr[1].split():
                        if attr_name in self.value_list:
                            self._process = True
                            self.attr = attr_name

    def handle_data(self, data):
        if self._process:
            self.data[self.attr] = data
            self._process = False

class Login(object):

    def __init__(self):
        self.name = ''
        self.passwprd = ''
        self.domain = ''

        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def setLoginInfo(self,username,password,domain):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password
        self.domain = domain

    def login(self):
        '''登录网站'''
        loginparams = {'domain':self.domain,'email':self.name, 'password':self.pwd}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        req = urllib2.Request(loginurl, urllib.urlencode(loginparams),headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        print(thePage)

if __name__ == '__main__':


    url="http://www.jisilu.cn/data/sfnew/#tlink_3"
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection':'close',
    'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
    }
    req_timeout = 5
    req = urllib2.Request(url,None,req_header)
    resp = urllib2.urlopen(req,None,req_timeout)
    html = unicode( resp.read() , errors='ignore')
    req = urllib2.Request(url,None,req_header)
    resp = urllib2.urlopen(req,None,req_timeout)
    html = unicode( resp.read() , errors='ignore')
    print(html)
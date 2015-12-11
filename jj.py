#  -*- coding: UTF-8 -*-
# Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
# Type "copyright", "credits" or "license()" for more information.
# >>> ================================ RESTART ================================

from HTMLParser import HTMLParser
import urllib2
import urllib
import re
from math import *
import base64
import time
import gzip
import StringIO
import sys
import os
import operator

reload(sys)
sys.setdefaultencoding('utf-8')
value_list = ["asset-value", "date"]
temp_list = []
asset_list= []

class FundDataParser(HTMLParser):
    def __init__(self, value_list = value_list):
        HTMLParser.__init__(self) # old-style class could not use super
        self._process = False
        self.value_list =  value_list
        self.attr = ""
        self.data = {}
        self.result = {}



    def get(self, code):
        find_re = re.compile(r'<div id="statuspzgz" class="fundpz"><span class=".+?">(.+?)</span>',re.DOTALL)
        time_re = re.compile(r'<p class="time">(.+?)</p>',re.DOTALL)
        ul="http://fund.eastmoney.com/%s.html" % (code)
        htmls=urllib2.urlopen(ul).read()
        print(code)
        print(find_re.findall(htmls))
        if str(find_re.findall(htmls)[0]) == '---':

             return(self.result)
        temp=str(find_re.findall(htmls)[0])

        header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','Accept':'application/json'}
        url = "http://finance.sina.com.cn/fund/quotes/%s/bc.shtml" % (code)
        #f = urllib2.urlopen(url)



        response = urllib2.urlopen(url)

        request = urllib2.Request(url, headers=randHeader())
        response = urllib2.urlopen(request)
        html = response.read()
        #html = html.decode('gbk').encode('utf-8')
        self.feed(html)
        self.close()
        #html = unicode(html, "gb2312").encode("utf8")
        self.result = self.data


        assetvalue=self.result.get('asset-value')
        if assetvalue is None:
            print("1")
            return(self.result)



        print(assetvalue)
        #time.sleep(0.1)
        temp=100*((float(temp)-float(assetvalue))/float(assetvalue))
        data=self.result.get('date')
        #temp="基金编码："+code+"  套利空间："+str(temp)+"  日期："+data
        temps=(code,temp,data)
        #print(temp)
        asset_list.append(temps)
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
import random

def randHeader():

    head_connection = ['Keep-Alive','close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5','en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']


    header = {
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0,len(head_user_agent))]
    }
    return header

print(randHeader())
def main():
   parser = FundDataParser()

   f = open(r'C:\tools\Python27\jj\text.txt','r')
   while True:
         line = f.readline()
         if line:
             pass
             # do something here
             line=line.strip('\n')
             parser.get(line)
             line=line.strip()
             p=line.rfind('.')
             filename=line[0:p]

         else:
                break
   f.close()

   #parser.get("150210")
   print(asset_list)
   asset_list.sort(key=operator.itemgetter(1),reverse=True)
   print(asset_list)

if __name__ == '__main__':
    main()
